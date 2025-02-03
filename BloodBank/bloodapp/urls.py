from django.urls import path
from .views import get_donors

urlpatterns = [
    path('api/donors/', get_donors, name='get_donors'),
]
