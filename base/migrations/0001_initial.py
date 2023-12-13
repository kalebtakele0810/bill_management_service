# Generated by Django 4.0 on 2023-12-13 13:34

import base.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('custom_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dueDate', models.DateField(max_length=200, validators=[base.models.no_past_due_date])),
                ('amount', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('PAID', 'Paid'), ('OVERDUE', 'Overdue')], default='PENDING', max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='custom_users.account')),
            ],
            options={
                'ordering': ['dueDate', '-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('transactionId', models.CharField(max_length=20)),
                ('paymentChannel', models.CharField(max_length=50)),
                ('remark', models.TextField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('bill', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.bill')),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
    ]
