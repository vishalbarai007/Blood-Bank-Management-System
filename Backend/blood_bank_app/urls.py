from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    login_view, DonorViewSet, BloodStockViewSet, 
    ContactViewSet, HospitalRequestViewSet
)

router = DefaultRouter()
router.register(r'donors', DonorViewSet)
router.register(r'blood-stock', BloodStockViewSet)
router.register(r'hospital-requests', HospitalRequestViewSet)
router.register(r'contacts', ContactViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login_view, name='login'),
]