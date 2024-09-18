# Generated by Django 5.1 on 2024-08-26 08:20

import base_model
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
            name='Employee',
            fields=[
                ('id', models.CharField(default=base_model.generate_nanoid, editable=False, max_length=20, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False, editable=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('contact_no', models.CharField(max_length=20)),
                ('address_street', models.TextField(max_length=100)),
                ('address_city', models.TextField(max_length=20)),
                ('cnic', models.CharField(max_length=13, verbose_name='CNIC')),
                ('emp_group', models.CharField(choices=[('exec', 'Executive'), ('tech', 'Technical'), ('staff', 'Office Staff'), ('marketing', 'Marketing'), ('sales', 'Sales')], max_length=10)),
                ('joining_date', models.DateTimeField(default=datetime.datetime.now)),
                ('resignation_date', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'employees',
                'abstract': False,
            },
        ),
    ]
