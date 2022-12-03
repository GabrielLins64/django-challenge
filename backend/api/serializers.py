from rest_framework import serializers, fields
from api.models import Vulnerability


class VulnerabilitySerializer(serializers.ModelSerializer):
    publication_date = fields.DateField(input_formats=['%Y-%m-%d'])

    class Meta:
        model = Vulnerability
        fields = [
            'asset_hostname',
            'asset_ip_address',
            'title',
            'severity',
            'cvss',
            'publication_date',
        ]
