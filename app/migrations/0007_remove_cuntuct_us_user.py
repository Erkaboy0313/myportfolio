# Generated by Django 4.1.7 on 2023-05-14 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_userinfo_experince'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuntuct_us',
            name='user',
        ),
    ]
