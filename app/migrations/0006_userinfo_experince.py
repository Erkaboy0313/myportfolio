# Generated by Django 4.1.7 on 2023-05-14 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_posttranslation_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='experince',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]