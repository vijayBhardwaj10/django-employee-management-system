# Generated by Django 2.2 on 2019-05-22 16:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ems_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HolidayModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(auto_now_add=True, verbose_name='Data rozpoczęcia')),
                ('end_date', models.DateField(verbose_name='Data zakończenia')),
                ('is_used', models.BooleanField(default=False)),
                ('is_approved', models.BooleanField(default=True)),
                ('approver_user', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='holiday_approver_user', to=settings.AUTH_USER_MODEL, verbose_name='Osoba zatwierdzająca')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='holiday_user', to=settings.AUTH_USER_MODEL, verbose_name='Pracownik')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=300, verbose_name='Nazwa klienta')),
                ('name', models.CharField(max_length=200, verbose_name='Nazwa')),
                ('number', models.IntegerField(verbose_name='Numer projektu')),
                ('number_2', models.IntegerField(verbose_name='Numer projektu 2')),
                ('project_type', models.CharField(max_length=50, verbose_name='Typ projektu')),
                ('status', models.CharField(max_length=50, verbose_name='Status')),
                ('start_date', models.DateField(verbose_name='Data rozpoczęcia')),
                ('end_date', models.DateField(verbose_name='Data zakończenia')),
                ('contact', models.CharField(max_length=500, verbose_name='Kontakt')),
                ('commants', models.CharField(blank=True, max_length=500, null=True, verbose_name='Uwagi')),
                ('id_employee', models.ManyToManyField(blank=True, null=True, related_name='project_employee_user', to=settings.AUTH_USER_MODEL, verbose_name='Pracownik')),
                ('id_project_pm', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='project_pm_user', to=settings.AUTH_USER_MODEL, verbose_name='Manager projektu')),
            ],
        ),
        migrations.DeleteModel(
            name='ProjectsModel',
        ),
    ]