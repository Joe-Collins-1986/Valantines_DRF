# Generated by Django 3.2.19 on 2024-02-18 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_account_image'),
        ('partnerprofile', '0006_auto_20240218_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partnerprofile',
            name='account',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='partner_profile', to='accounts.account'),
        ),
    ]
