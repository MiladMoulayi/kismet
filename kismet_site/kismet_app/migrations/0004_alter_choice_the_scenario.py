# Generated by Django 4.1.4 on 2023-01-14 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kismet_app', '0003_rename_scenario_choice_the_scenario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='the_scenario',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='kismet_app.scenario'),
        ),
    ]
