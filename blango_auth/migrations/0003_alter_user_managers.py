# Generated by Django 3.2.6 on 2023-04-11 11:25

import blango_auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blango_auth', '0002_auto_20221114_0245'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', blango_auth.models.BlangoUserManager()),
            ],
        ),
    ]
