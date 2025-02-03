from django.http import JsonResponse
from .models import Donor

def get_donors(request):
    donors = list(Donor.objects.values())
    return JsonResponse(donors, safe=False)
