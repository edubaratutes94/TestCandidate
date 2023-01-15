# Generated by Django 4.0 on 2023-01-15 03:57

import TestApp.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last Name')),
                ('ci', models.CharField(max_length=11, unique=True, validators=[TestApp.utils.validate_carne], verbose_name='ID')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('age', models.IntegerField(validators=[TestApp.utils.validate_only_numbers], verbose_name='Age')),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='YearExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('year', models.IntegerField(validators=[TestApp.utils.validate_only_numbers], verbose_name='Years of experience')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TestApp.candidates', verbose_name='Technology')),
                ('technology', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TestApp.technology', verbose_name='Technology')),
            ],
        ),
        migrations.AddField(
            model_name='candidates',
            name='sex',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TestApp.technology'),
        ),
    ]