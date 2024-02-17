
from rest_framework import generics
from main.permissions import IsOwnerDocsOnly, IsOwnerOrReadOnly
from .models import Account
from .serializers import AccountSerializer


class AccountList(generics.ListAPIView):
    """
    - List out all the accounts
    - Profile created by user registration so no create
    account required
    - Only allow CRUD on the user's own account
    """
    serializer_class = AccountSerializer
    permission_classes = [IsOwnerDocsOnly]
    queryset = Account.objects.filter().order_by('-created_at')

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
