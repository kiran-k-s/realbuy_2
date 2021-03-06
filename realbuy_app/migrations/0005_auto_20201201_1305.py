# Generated by Django 3.1.3 on 2020-12-01 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realbuy_app', '0004_auto_20201127_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='availability',
            field=models.CharField(choices=[('ready to move', 'Ready to Move'), ('under construction', 'Under Construction')], max_length=100),
        ),
        migrations.AlterField(
            model_name='property',
            name='built_up_unit',
            field=models.CharField(choices=[('cm', 'sq.cm'), ('m', 'sq.m'), ('ft', 'sq.ft')], max_length=100),
        ),
        migrations.AlterField(
            model_name='property',
            name='carpet_unit',
            field=models.CharField(choices=[('cm', 'sq.cm'), ('m', 'sq.m'), ('ft', 'sq.ft')], max_length=100),
        ),
        migrations.AlterField(
            model_name='property',
            name='resale_or_new',
            field=models.CharField(choices=[('resale', 'Resale'), ('new', 'New Booking')], default=('resale', 'Resale'), max_length=100),
        ),
        migrations.AlterField(
            model_name='property',
            name='sell_or_rent',
            field=models.CharField(choices=[('sell', 'Sell'), ('rent', 'Rent')], max_length=100),
        ),
    ]
