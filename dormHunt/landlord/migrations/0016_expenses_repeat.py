# Generated by Django 3.0.1 on 2020-02-25 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landlord', '0015_auto_20200224_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses',
            name='repeat',
            field=models.BooleanField(default=False),
        ),
    ]
