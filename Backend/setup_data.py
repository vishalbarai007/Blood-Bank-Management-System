import os
import django
import sys
from datetime import datetime

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blood_bank_project.settings')
django.setup()

from django.contrib.auth.models import User
from blood_bank_app.models import BloodStock, UserProfile

# Create admin user
if not User.objects.filter(username='admin').exists():
    admin_user = User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    UserProfile.objects.create(user=admin_user, user_type='admin')
    print("Admin user created")

# Create regular user
if not User.objects.filter(username='user').exists():
    regular_user = User.objects.create_user('user', 'user@example.com', 'user123')
    UserProfile.objects.create(user=regular_user, user_type='user')
    print("Regular user created")

# Initialize blood stock for all blood groups
blood_groups = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
for bg in blood_groups:
    BloodStock.objects.get_or_create(blood_group=bg, defaults={'quantity': 0})
    print(f"Blood stock for {bg} initialized")

print("Setup completed successfully!")