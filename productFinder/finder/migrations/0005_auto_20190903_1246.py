# Generated by Django 2.2.3 on 2019-09-03 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0004_auto_20190903_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='logo',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='position',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]