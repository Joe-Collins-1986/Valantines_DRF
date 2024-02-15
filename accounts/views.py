from django.db.models import Count
from rest_framework import generics, filters
from main.permissions import IsOwnerOrReadOnly
from .models import Account
from .serializers import AccountSerializer
from django_filters.rest_framework import DjangoFilterBackend


class AccountList(generics.ListAPIView):
    """
    - List out all the accounts
    - Profile created by user registration so no create
    account required
    - Accounts are not to be deleted unless User is
    removed so no delete functionality required
    - Due to no create, update, delete no permission class required
    """
    serializer_class = AccountSerializer
    queryset = Account.objects.all().order_by('-created_at')

    filter_backends = [
        filters.SearchFilter,
    ]

    search_fields = [
        'profile_name',
    ]

class AccountDetail(generics.RetrieveUpdateAPIView):
    """
    - Detail the specificly requested account
    - Uses same Accounts serializer
    - Uses IsOwnerOrReadOnly tailored permission class
    to ensure only owner can update profile info
    """
    serializer_class = AccountSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Account.objects.all().order_by('-created_at')
