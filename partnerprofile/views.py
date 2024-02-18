from rest_framework import generics
from main.permissions import IsOwnerOrReadOnly, IsAccountOrReadOnly
from .models import PartnerProfile
from .serializers import PartnerProfileSerializer


class PartnerProfileList(generics.ListAPIView):
    """
    - List out all the accounts
    - Account created by user registration so no create
    account required
    """
    serializer_class = PartnerProfileSerializer
    queryset = PartnerProfile.objects.all().order_by('-created_at')
    

class PartnerProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    - Detail the specificly requested account
    - Uses same Accounts serializer
    - Uses IsOwnerOrReadOnly tailored permission class
    to ensure only owner can update profile info
    """
    serializer_class = PartnerProfileSerializer
    permission_classes = [IsAccountOrReadOnly]
    queryset = PartnerProfile.objects.all().order_by('-created_at')