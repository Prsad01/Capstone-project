# Generated by Django 4.2.7 on 2023-11-12 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='BookingDate',
            new_name='bookingDate',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='No_of_guests',
            new_name='no_of_guests',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='Inventory',
            new_name='inventory',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='Price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='Title',
            new_name='title',
        ),
    ]