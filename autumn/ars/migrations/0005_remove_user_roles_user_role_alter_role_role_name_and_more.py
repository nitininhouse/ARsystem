# Generated by Django 5.1.1 on 2024-10-10 04:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ars', '0004_alter_role_role_name_userrole'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='roles',
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ars.role'),
        ),
        migrations.AlterField(
            model_name='role',
            name='role_name',
            field=models.CharField(choices=[('admin', 'Admin'), ('reviewer', 'Reviewer'), ('reviewee', 'Reviewee')], max_length=20, unique=True),
        ),
        migrations.DeleteModel(
            name='UserRole',
        ),
    ]
