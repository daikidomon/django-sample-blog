# Generated by Django 4.0 on 2021-12-24 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, db_column='image', null=True, upload_to='images/'),
        ),
    ]