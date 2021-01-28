from django.urls import path
from .views import ContactApi

urlpatterns = [
    path('contact/', ContactApi.as_view())
]