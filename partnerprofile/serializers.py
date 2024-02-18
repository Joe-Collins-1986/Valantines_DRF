from rest_framework import serializers
from .models import PartnerProfile



class PartnerProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the PartnerProfile model
    Owner shows object owner's username in readonly format
    Get function to set is_owner to true/false
    """

    created_by = serializers.ReadOnlyField(source='account.account_name')
    created_by_id = serializers.ReadOnlyField(source='account.id')
    partner_id = serializers.ReadOnlyField(source='id')

    is_partner = serializers.SerializerMethodField()

    def get_is_partner(self, obj):
        request = self.context['request']
        return request.user == obj.account.owner


    class Meta:
        model = PartnerProfile
        fields = [
            'created_by', 'created_by_id', 'partner_id', 'age', 'zodiac_sign',
            'relationship', 'characteristics', 'interests',
            'location', 'is_partner'
        ]
