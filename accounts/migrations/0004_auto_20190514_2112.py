# Generated by Django 2.2 on 2019-05-14 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190514_2038'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myuser',
            options={},
        ),
        migrations.RenameField(
            model_name='useraccess',
            old_name='user_id',
            new_name='user',
        ),
    ]