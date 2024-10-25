# bit_mailer/views.py

from rest_framework import generics
from .models import MailRequest
from .serializers import MailRequestSerializer

# API View for creating MailRequest
class MailRequestCreateView(generics.CreateAPIView):
    queryset = MailRequest.objects.all()
    serializer_class = MailRequestSerializer

# API View for listing MailRequests
class MailRequestListView(generics.ListAPIView):
    queryset = MailRequest.objects.all()
    serializer_class = MailRequestSerializer
