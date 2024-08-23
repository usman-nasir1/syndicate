# Generated by Django 5.1 on 2024-08-23 20:59

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Salary id')),
                ('gross_salary', models.FloatField(default=0.0, verbose_name='Gross Salary')),
                ('is_active', models.BooleanField(default=True)),
                ('effective_from', models.DateField(default=datetime.date.today)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='modified_by', to=settings.AUTH_USER_MODEL)),
                ('updated_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='updated_from', to='finances.salary')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='salary', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'salaries',
                'abstract': False,
            },
        ),
    ]
