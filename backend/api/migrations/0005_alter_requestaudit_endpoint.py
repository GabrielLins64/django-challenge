# Generated by Django 4.1 on 2022-12-10 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_requestaudit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestaudit',
            name='endpoint',
            field=models.CharField(max_length=300, null=True),
        ),
    ]