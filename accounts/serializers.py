from rest_framework import serializers
from .models import Account



class AccountSerializer(serializers.ModelSerializer):
    """
    Serializer for the Account model
    Owner shows object owner's username in readonly format
    Get function to set is_owner to true/false
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Account
        fields = [
            'id', 'owner', 'created_at',
            'account_name', 'bio', 'image',
            'is_owner'
        ]
