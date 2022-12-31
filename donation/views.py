from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PersonSerializer, DonationSerializer
from .models import Person, Donation

class PersonView(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class DonationView(viewsets.ModelViewSet):
    serializer_class = DonationSerializer
    queryset = Donation.objects.all()