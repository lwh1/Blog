# Generated by Django 2.2.5 on 2021-02-04 11:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20210203_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 4, 11, 43, 7, 879806, tzinfo=utc)),
        ),
    ]
