# Generated by Django 3.0.3 on 2020-09-03 16:20

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email_address', models.EmailField(default='admin@admin.com', max_length=255, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Varification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_varification', models.CharField(max_length=20, null=True)),
                ('phone_varification', models.CharField(max_length=20, null=True)),
                ('created_dt', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('updated_dt', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('email_address', models.OneToOneField(default='admin@admin.com', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='email_address')),
            ],
        ),
        migrations.CreateModel(
            name='PhoneOtp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_otp', models.IntegerField()),
                ('counter', models.IntegerField()),
                ('email_address', models.OneToOneField(default='admin@admin.com', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='email_address')),
            ],
        ),
    ]
