from rest_framework import generics
from .models import Account, Activity,ActivityStatus,Contact,ContactSource,ContactStatus
from .serializers import AccountSerializer,ActivitySerializer, ActivityStatusSerializer, ContactSerializer,ContactSourceSerializer,ContactStatusSerializer


class AccountAPIView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class ActivityAPIView(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class ActivityStatusAPIView(generics.ListCreateAPIView):
    queryset = ActivityStatus.objects.all()
    serializer_class = ActivityStatusSerializer

class ContactAPIView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactStatusAPIView(generics.ListCreateAPIView):
    queryset = ContactStatus.objects.all()
    serializer_class = ContactStatusSerializer

class ContactSourceAPIView(generics.ListCreateAPIView):
    queryset = ContactSource.objects.all()
    serializer_class = ContactSourceSerializer