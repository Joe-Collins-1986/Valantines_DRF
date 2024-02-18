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
    owner = models.OneToOneField(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    birthday = models.DateField()
    zodiac_sign = models.CharField(max_length=50, choices=ZODIAC)
    relationship = models.CharField(max_length=50, choices=RELATIONSHIP)
    characteristics = models.CharField(max_length=50, choices=CHARACTERISTICS)
    interests = models.CharField(max_length=50, choices=INTERESTS)
    location = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.account} partner's account"
