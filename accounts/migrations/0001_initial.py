# Generated by Django 3.2.24 on 2024-02-15 15:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('account_name', models.CharField(blank=True, max_length=50)),
                ('bio', models.TextField(blank=True)),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], default='../images/accountImages/default-account-img.jpeg', force_format='JPEG', keep_meta=True, quality=-1, scale=None, size=[150, 150], upload_to='images/accountImages/')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
