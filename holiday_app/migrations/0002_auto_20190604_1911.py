# Generated by Django 2.2 on 2019-06-04 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('holiday_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holidaymodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='holiday_user', to=settings.AUTH_USER_MODEL, verbose_name='Pracownik'),
        ),
    ]