from django.db import models
from django.contrib.auth.models import User

# Add a user profile to extend the built-in User model
class UserProfile(models.Model):
    USER_TYPES = [
        ('admin', 'Admin'),
        ('user', 'Regular User'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='user')
    
    def __str__(self):
        return f"{self.user.username} - {self.user_type}"

class Donor(models.Model):
    BLOOD_GROUPS = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    donation_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.blood_group}"

class BloodStock(models.Model):
    blood_group = models.CharField(max_length=3, unique=True)
    quantity = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.blood_group}: {self.quantity} units"

class HospitalRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    
    hospital_name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=3)
    quantity = models.IntegerField()
    patient_name = models.CharField(max_length=100)
    patient_age = models.IntegerField()
    reason = models.TextField()
    contact_person = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=15)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    request_date = models.DateTimeField(auto_now_add=True)
    processed_date = models.DateTimeField(null=True, blank=True)
    processed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.hospital_name} - {self.blood_group} ({self.quantity} units) - {self.status}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.subject}"