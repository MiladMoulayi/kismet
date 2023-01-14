from django.db import models

# Create your models here.
class Character(models.Model):
  name = models.CharField(primary_key=True, max_length=200)
  ALIGNMENTS = (
    ('E', 'Evil'),
    ('N', 'Neutral'),
    ('G', 'Good'),
  )
  alignment = models.CharField(max_length=1, choices=ALIGNMENTS, default='N')


class Scenario(models.Model):
  scenario_id = models.AutoField(primary_key=True)
  characterName = models.ForeignKey(Character, on_delete=models.CASCADE)
  description = models.TextField()
  # name = models.CharField(max_length=255)
  # description = models.CharField(max_length=255)
  # option1 = models.CharField(max_length=200, default='add')
  # option2 = models.CharField(max_length=200, default='add')
  # option3 = models.CharField(max_length=200, default='add')
  # winning_option = models.CharField(max_length=200, default='add')

  def __str__(self):
      return self.name

class Choice(models.Model):
  choice_id = models.AutoField(primary_key=True)
  scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE)
  option1 = models.CharField(max_length=200)
  option2 = models.CharField(max_length=200)
  option3 = models.CharField(max_length=200)
  # name = models.CharField(max_length=255)
  # type = models.CharField(max_length=255)

class Outcome(models.Model):
  outcome_id = models.AutoField(primary_key=True)
  choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
  win = models.CharField(max_length=200)
  lose = models.CharField(max_length=200)
  # name = models.CharField(max_length=255)
  # type = models.CharField(max_length=255)