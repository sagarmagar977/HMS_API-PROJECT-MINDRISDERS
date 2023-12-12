# Generated by Django 3.2.23 on 2023-12-05 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('frontdesk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.FloatField()),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontdesk.guestinfo')),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid_ampunt', models.FloatField()),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.bills')),
            ],
        ),
    ]
