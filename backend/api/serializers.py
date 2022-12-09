from rest_framework import serializers, fields
from django.contrib.auth.models import User
import io, csv

from api.models import Vulnerability


class VulnerabilitySerializer(serializers.ModelSerializer):
    """
    Vulnerability serializer for creating and retrieving data;
    """
    publication_date = fields.DateField(input_formats=['%Y-%m-%d'],
                                        required=False,
                                        allow_null=True)

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


class FileUploadSerializer(serializers.Serializer):
    """
    File serializer for retrieving file form a POST request
    """
    file = serializers.FileField()

    class Meta:
        fields = ('file',)


class VulnerabilityCSVSerializer:
    """
    Vulnerabilities CSV serializer that validates each CSV row
    in order to ensure the proper format of the Vulnerability.
    """
    def __init__(self, file, context: dict):
        decoded_file = file.read().decode()
        io_string = io.StringIO(decoded_file)

        self.reader = csv.reader(io_string)
        next(self.reader, None)
        self.vulnerabilities = []
        self.context = context
        self.errors = []

    def is_valid(self, raise_exception: bool = False):
        for row in self.reader:
            data = {
                "asset_hostname": row[0],
                "asset_ip_address": row[1],
                "title": row[2],
                "severity": row[3],
                "cvss": row[4] or None,
                "publication_date": row[5] or None,
            }
            serializer = VulnerabilitySerializer(data=data,
                                                 context=self.context)
            if serializer.is_valid():
                self.vulnerabilities.append(serializer.data)
            else:
                self.errors.append(serializer.errors)

                if raise_exception:
                    raise Exception(self.errors)
                else:
                    return False

        return True

    def save(self):
        for data in self.vulnerabilities:
            vulnerability = Vulnerability(**data)
            vulnerability.save()
