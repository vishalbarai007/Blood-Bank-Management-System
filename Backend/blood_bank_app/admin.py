from django.contrib import admin
from .models import Donor, BloodStock, Contact, HospitalRequest, UserProfile

class DonorAdmin(admin.ModelAdmin):
    list_display = ('name', 'blood_group', 'age', 'phone', 'donation_date')
    list_filter = ('blood_group', 'donation_date')
    search_fields = ('name', 'phone', 'email')

class BloodStockAdmin(admin.ModelAdmin):
    list_display = ('blood_group', 'quantity', 'last_updated')

class HospitalRequestAdmin(admin.ModelAdmin):
    list_display = ('hospital_name', 'blood_group', 'quantity', 'status', 'request_date')
    list_filter = ('blood_group', 'status', 'request_date')
    search_fields = ('hospital_name', 'patient_name', 'contact_person')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'date_submitted')
    list_filter = ('date_submitted',)
    search_fields = ('name', 'email', 'subject')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type')
    list_filter = ('user_type',)
    search_fields = ('user__username',)

admin.site.register(Donor, DonorAdmin)
admin.site.register(BloodStock, BloodStockAdmin)
admin.site.register(HospitalRequest, HospitalRequestAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(UserProfile, UserProfileAdmin)