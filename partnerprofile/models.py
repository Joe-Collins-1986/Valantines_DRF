from django.db import models
from accounts.models import Account
from .zodiac import ZODIAC
from .relationship import RELATIONSHIP
from .characteristics import CHARACTERISTICS
from .interests import INTERESTS


class PartnerProfile(models.Model):
    """
    PartnerProfile Model:
    """
    account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='partner_profile')
    name = models.CharField(max_length=50, blank=True)
    age = models.CharField(max_length=50, blank=True)
    zodiac_sign = models.CharField(max_length=50, choices=ZODIAC, blank=True)
    relationship = models.CharField(max_length=50, choices=RELATIONSHIP, blank=True)
    characteristics = models.CharField(max_length=50, choices=CHARACTERISTICS, blank=True)
    interests = models.CharField(max_length=50, choices=INTERESTS, blank=True)
    location = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.account.account_name}'s partner's account"
