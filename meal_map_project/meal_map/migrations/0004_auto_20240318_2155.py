# Generated by Django 2.2.28 on 2024-03-18 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meal_map', '0003_delete_userprofile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='restaurantowner',
            options={'verbose_name_plural': 'RestaurantOwners'},
        ),
    ]