from rest_framework import serializers
from .models import PartnerProfile



class PartnerProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the PartnerProfile model
    Owner shows object owner's username in readonly format
    Get function to set is_owner to true/false
    """

    account = serializers.ReadOnlyField(source='account.username')
    is_account = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = PartnerProfile
        fields = '__all__'
        