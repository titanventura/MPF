# Generated by Django 2.2.3 on 2019-08-19 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='brand',
            new_name='prodbrand',
        ),
    ]
