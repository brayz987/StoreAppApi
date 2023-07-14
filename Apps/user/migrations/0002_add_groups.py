# Generated by Django 4.2.2 on 2023-06-09 00:16

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


def apply_migration(apps, schema_editor):
    User = apps.get_model('user', 'CustomUserModel')
    Permission = apps.get_model('auth', 'Permission')
    permission_list = Permission.objects.all()
    Group = apps.get_model('auth', 'Group')

    administrator_group = Group(name=u'administrator')
    administrator_group.save()
    customer_group = Group(name=u'customer')
    customer_group.save()

    administrator_group.permissions.set(permission_list)
    customer_group.permissions.set(permission_list)

    for user in User.objects.all():
        customer_group.user_set.add(user)


def revert_migration(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.filter(
        name__in=[
            u'administrator',
            u'customer'
        ]
    ).delete()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(apply_migration,revert_migration)
    ]