from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Donor, BloodStock, Contact, HospitalRequest, UserProfile
from .serializers import (
    UserSerializer, DonorSerializer, BloodStockSerializer, 
    ContactSerializer, HospitalRequestSerializer
)

class IsAdmin(IsAuthenticated):
    """
    Custom permission to only allow admin users to access the view.
    """
    def has_permission(self, request, view):
        is_authenticated = super().has_permission(request, view)
        if not is_authenticated:
            return False
        
        try:
            return request.user.profile.user_type == 'admin'
        except UserProfile.DoesNotExist:
            return False

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(username=username, password=password)
    
    if user:
        try:
            profile = user.profile
            return Response({
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'user_type': profile.user_type
            })
        except UserProfile.DoesNotExist:
            # Create a default profile if it doesn't exist
            profile = UserProfile.objects.create(user=user, user_type='user')
            return Response({
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'user_type': profile.user_type
            })
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class DonorViewSet(viewsets.ModelViewSet):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        
        # Update blood stock when a new donor is added
        blood_group = request.data.get('blood_group')
        if blood_group:
            try:
                stock = BloodStock.objects.get(blood_group=blood_group)
                stock.quantity += 1
                stock.save()
            except BloodStock.DoesNotExist:
                BloodStock.objects.create(blood_group=blood_group, quantity=1)
        
        return response

class BloodStockViewSet(viewsets.ModelViewSet):
    queryset = BloodStock.objects.all()
    serializer_class = BloodStockSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

class HospitalRequestViewSet(viewsets.ModelViewSet):
    queryset = HospitalRequest.objects.all().order_by('-request_date')
    serializer_class = HospitalRequestSerializer
    
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAdmin]
        elif self.action == 'create':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdmin]
        return [permission() for permission in permission_classes]
    
    @action(detail=True, methods=['post'])
    def process_request(self, request, pk=None):
        hospital_request = self.get_object()
        status_action = request.data.get('status')
        
        if status_action not in ['approved', 'rejected']:
            return Response(
                {'error': 'Invalid status. Must be "approved" or "rejected".'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # If approving, check if enough blood is available
        if status_action == 'approved':
            try:
                blood_stock = BloodStock.objects.get(blood_group=hospital_request.blood_group)
                if blood_stock.quantity < hospital_request.quantity:
                    return Response(
                        {'error': f'Not enough {hospital_request.blood_group} blood in stock.'}, 
                        status=status.HTTP_400_BAD_REQUEST
                    )
                
                # Update blood stock
                blood_stock.quantity -= hospital_request.quantity
                blood_stock.save()
            except BloodStock.DoesNotExist:
                return Response(
                    {'error': f'No {hospital_request.blood_group} blood in stock.'}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
        
        # Update request status
        hospital_request.status = status_action
        hospital_request.processed_date = timezone.now()
        hospital_request.processed_by = request.user
        hospital_request.save()
        
        return Response(HospitalRequestSerializer(hospital_request).data)

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]  # Allow anyone to submit contact forms
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'destroy']:
            permission_classes = [IsAdmin]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]