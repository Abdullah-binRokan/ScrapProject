# Generated by Django 5.1.4 on 2024-12-15 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profileseller_specialized'),
        ('autoparts', '0004_product_delivery_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileseller',
            name='specialized',
        ),
        migrations.AddField(
            model_name='profileseller',
            name='specializaties',
            field=models.ManyToManyField(to='autoparts.category'),
        ),
    ]