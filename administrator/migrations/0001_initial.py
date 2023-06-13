# Generated by Django 4.2.1 on 2023-06-01 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='username')),
                ('email', models.EmailField(max_length=150, unique=True, verbose_name='email')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='name')),
                ('last_name', models.CharField(blank=True, max_length=100, verbose_name='last_name')),
                ('user_active', models.BooleanField(default=True)),
                ('user_administrator', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'administradores',
            },
        ),
    ]