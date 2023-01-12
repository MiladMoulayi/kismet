# Generated by Django 4.1.4 on 2023-01-10 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kismet_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='alignment',
            field=models.CharField(choices=[('E', 'Evil'), ('N', 'Neutral'), ('G', 'Good')], default='N', max_length=1),
        ),
    ]