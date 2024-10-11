# Generated by Django 5.1.1 on 2024-10-09 14:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ars', '0003_alter_role_role_name_delete_userrole'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='role_name',
            field=models.CharField(choices=[('admin', 'Admin'), ('reviewer', 'Reviewer'), ('reviewee', 'Reviewee')], max_length=20),
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ars.role')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ars.user')),
            ],
        ),
    ]
