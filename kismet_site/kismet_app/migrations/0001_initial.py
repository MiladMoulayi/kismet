# Generated by Django 4.1.4 on 2023-01-14 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('alignment', models.CharField(choices=[('E', 'Evil'), ('N', 'Neutral'), ('G', 'Good')], default='N', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Outcome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('option1', models.CharField(default='add', max_length=200, null=True)),
                ('option2', models.CharField(default='add', max_length=200, null=True)),
                ('option3', models.CharField(default='add', max_length=200, null=True)),
                ('winning_option', models.CharField(default='add', max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('scenario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kismet_app.scenario')),
            ],
        ),
    ]
