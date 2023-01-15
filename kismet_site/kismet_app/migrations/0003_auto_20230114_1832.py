# Generated by Django 4.1.4 on 2023-01-15 02:32

from django.db import migrations

from django.db import migrations, models

def load_data(apps, schema_editor):
    Scenario = apps.get_model('kismet_app', 'Scenario')
    Choice = apps.get_model('kismet_app', 'Choice')
    Outcome = apps.get_model('kismet_app', 'Outcome')
    academic_honesty = Scenario.objects.create(
        name = 'Academic Honesty',
        description = 'You\'ve woken up, did your usual morning routine, and leave your house to go to school. Upon your arrival at school, one of your classmates asks to see your homework. What do you do?')
    academic_honesty.save()
    academic_choice_1 = Choice.objects.create(
        name = 'Tell him no.',
        type = 'Good',
        the_scenario = academic_honesty
    )
    academic_choice_1.save()
    academic_choice_2 = Choice.objects.create(
        name = 'Tell the teacher.',
        type = 'Neutral',
        the_scenario = academic_honesty
    )
    academic_choice_2.save()
    academic_choice_3 = Choice.objects.create(
        name = 'Let him see it.',
        type = 'Evil',
        the_scenario = academic_honesty
    )
    academic_choice_3.save()
    academic_outcome_1 = Outcome.objects.create(
        name = 'Your classmate has become enraged. He proceeds to yell insults and threats at you. All of this commotion has led to your teacher to intervene. She asks you “what\'s wrong?”',
        type = 'Good',
        choices = [Choice.objects.create(name='Tell her nothing and head to class.', type='Good'), Choice.objects.create(name='Tell her What your classmate wanted and what he said.', type='Good')]
    )
    academic_outcome_1.save()
    academic_outcome_2 = Outcome.objects.create(
        name = 'You open up your backpack and allow your classmate to see your homework. The moment your classmate has your homework in his possession he puts it in his backpack and walks to class. What do you do now?',
        type = 'Evil',
        choices = [Choice.objects.create(name='His back is turned. Time to strike!', type='Evil'), Choice.objects.create(name='Go to class and tell the professor what happened.', type='Good'), Choice.objects.create(name='Call your classmate back and tell him that you want your homework back', type='Neutral')]
    )
    academic_outcome_2.save()
    # need_outcome_3 = Outcome.objects.create(
    #     name = 'Your neighbor cusses you out for making fun of him and the next day you find that your car has been keyed',
    #     type = 'Evil'
    # )
    # need_outcome_3.save()

def delete_data(apps, schema_editor):
    Scenario = apps.get_model('kismet_app', 'Scenario')
    Scenario.objects.all().delete()
    Choice = apps.get_model('kismet_app', 'Choice')
    Choice.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('kismet_app', '0002_auto_20230114_1647'),
    ]

    operations = [
        migrations.RunPython(load_data, delete_data)
    ]
