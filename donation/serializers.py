from rest_framework import serializers
from .models import Person, Donation

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('person_id', 'person_name', 'person_document', 'person_address', 'person_photo', 'person_phone')


class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ('donation_name', 'donation_description', 'donation_photo', 'user', 'category', 'detail', 'campaign')