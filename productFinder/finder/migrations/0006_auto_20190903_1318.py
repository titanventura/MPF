# Generated by Django 2.2.3 on 2019-09-03 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0005_auto_20190903_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='position',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
