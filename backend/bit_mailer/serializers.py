# bit_mailer/serializers.py

from rest_framework import serializers
from .models import MailRequest

class MailRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MailRequest
        fields = '__all__'
