from django.db import models


class Vulnerability(models.Model):
    asset_hostname = models.CharField(max_length=20)
    asset_ip_address = models.GenericIPAddressField()
    title = models.CharField(max_length=300)
    severity = models.CharField(max_length=10)
    cvss = models.FloatField(blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)
    fixed = models.BooleanField(default=False)


class CVSSRatings(models.Model):
    text = models.CharField(max_length=10)
    base_score_min = models.FloatField()
    base_score_max = models.FloatField()
