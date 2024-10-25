# bit_mailer/urls.py

from django.urls import path
from .views import MailRequestCreateView, MailRequestListView

urlpatterns = [
    path('api/mail_request/', MailRequestCreateView.as_view(), name='mail_request_create'),
    path('api/submissions/', MailRequestListView.as_view(), name='submissions_list'),
]
