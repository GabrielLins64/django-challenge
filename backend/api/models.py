from django.db import models
from django.contrib.auth.models import User


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


class RequestAudit(models.Model):
    endpoint = models.CharField(max_length=300, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    response_code = models.PositiveSmallIntegerField()
    method = models.CharField(max_length=10, null=True)
    remote_address = models.GenericIPAddressField(null=True)
    exec_time = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now=True)
