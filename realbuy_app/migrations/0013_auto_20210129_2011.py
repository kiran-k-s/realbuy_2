# Generated by Django 3.1.3 on 2021-01-29 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realbuy_app', '0012_auto_20210105_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='property_floor',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
