from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Donor, BloodStock, Contact, HospitalRequest, UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user_type']

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile']

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = '__all__'

class BloodStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodStock
        fields = '__all__'

class HospitalRequestSerializer(serializers.ModelSerializer):
    processed_by_username = serializers.SerializerMethodField()
    
    class Meta:
        model = HospitalRequest
        fields = '__all__'
    
    def get_processed_by_username(self, obj):
        if obj.processed_by:
            return obj.processed_by.username
        return None

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'