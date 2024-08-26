# Generated by Django 5.1 on 2024-08-26 08:20

import base_model
import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('id', models.CharField(default=base_model.generate_nanoid, editable=False, max_length=20, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('is_active', models.BooleanField(default=True)),
                ('effective_from', models.DateField(default=datetime.date.today)),
                ('name', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(choices=[('travel', 'Travel'), ('residence', 'Residence'), ('food', 'Food'), ('vending_machine', 'Vending Machine'), ('telecom', 'Telecom Balance'), ('insurance', 'Insurance')], max_length=50, null=True)),
                ('benefit_amount', models.FloatField(default=0, null=True, verbose_name='Benefit Amount')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_salary', to='employees.employee')),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL)),
                ('updated_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='updated_from', to='finances.benefit')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_salary', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'benefits',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.CharField(default=base_model.generate_nanoid, editable=False, max_length=20, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('is_active', models.BooleanField(default=True)),
                ('effective_from', models.DateField(default=datetime.date.today)),
                ('gross_salary', models.FloatField(default=0.0, verbose_name='Gross Salary')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_salary', to='employees.employee')),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL)),
                ('updated_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='updated_from', to='finances.salary')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_salary', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'salaries',
                'abstract': False,
            },
        ),
    ]
