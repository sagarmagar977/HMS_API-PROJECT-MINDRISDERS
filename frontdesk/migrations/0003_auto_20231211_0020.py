# Generated by Django 3.2.23 on 2023-12-10 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontdesk', '0002_auto_20231206_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestinfo',
            name='phone_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='room',
            name='room_no',
            field=models.IntegerField(default=0),
        ),
    ]
