# Generated by Django 4.1.4 on 2023-01-14 20:14

from django.db import migrations, models

def load_data(apps, schema_editor):
    Scenario = apps.get_model('kismet_app', 'Scenario')
    Choice = apps.get_model('kismet_app', 'Choice')
    Outcome = apps.get_model('kismet_app', 'Outcome')
    in_time_of_need = Scenario.objects.create(
        name = 'In Time of Need',
        description = 'Decide whether or not to help your neighbor jumpstart his car'
    )
    in_time_of_need.save()
    need_choice_1 = Choice.objects.create(
        name = 'Get your jumper cables and help him',
        type = 'Good',
        the_scenario = in_time_of_need
    )
    need_choice_1.save()
    need_choice_2 = Choice.objects.create(
        name = 'Ignore him and continue to your car',
        type = 'Neutral',
        the_scenario = in_time_of_need
    )
    need_choice_2.save()
    need_choice_3 = Choice.objects.create(
        name = 'Laugh at him and tell him that\'s what he gets for buying a Ford',
        type = 'Evil',
        the_scenario = in_time_of_need
    )
    need_choice_3.save()
    need_outcome_1 = Outcome.objects.create(
        name = 'Your neighbor views you as a reliable person and offers you free Uber rides in the future',
        type = 'Good'
    )
    need_outcome_1.save()
    need_outcome_2 = Outcome.objects.create(
        name = 'Your neighbor views you as someone who is not concerned with the suffering of others and ignores you in future interactions',
        type = 'Neutral'
    )
    need_outcome_2.save()
    need_outcome_3 = Outcome.objects.create(
        name = 'Your neighbor cusses you out for making fun of him and the next day you find that your car has been keyed',
        type = 'Evil'
    )
    need_outcome_3.save()

def delete_data(apps, schema_editor):
    Scenario = apps.get_model('kismet_app', 'Scenario')
    Scenario.objects.all().delete()
    Choice = apps.get_model('kismet_app', 'Choice')
    Choice.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('kismet_app', '0007_outcome_choices'),
    ]

    operations = [
        migrations.RunPython(load_data, delete_data),
    ]
