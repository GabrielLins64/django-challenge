from django.db import models
from django.utils import timezone


class Vulnerability(models.Model):
    asset_hostname = models.CharField(max_length=20)
    asset_ip_address = models.GenericIPAddressField()
    title = models.CharField(max_length=300)
    severity = models.CharField(max_length=10)
    cvss = models.FloatField()
    publication_date = models.DateField(default=timezone.now)
    fixed = models.BooleanField(default=False)


class CVSSRatings(models.Model):
    text = models.CharField(max_length=10)
    base_score_min = models.FloatField()
    base_score_max = models.FloatField()
