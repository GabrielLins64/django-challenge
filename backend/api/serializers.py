from rest_framework import serializers, fields
from django.contrib.auth.models import User

from api.models import Vulnerability


class VulnerabilitySerializer(serializers.ModelSerializer):
    """
    Vulnerability serializer for creating and retrieving data;
    """
    publication_date = fields.DateField(input_formats=['%Y-%m-%d'])

    class Meta:
        model = Vulnerability
        fields = [
            'id',
            'asset_hostname',
            'asset_ip_address',
            'title',
            'severity',
            'cvss',
            'publication_date',
            'fixed',
        ]


class VulnerabilityStatusSerializer(serializers.ModelSerializer):
    """
    Vulnerability status for updating only the vulnerability's status.
    """
    fixed = serializers.BooleanField(required=True)

    class Meta:
        model = Vulnerability
        fields = ['fixed']


class UserSerializer(serializers.ModelSerializer):
    """
    User serializer for fetching user data
    """
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'id',
            'is_staff',
            'is_active'
        ]
