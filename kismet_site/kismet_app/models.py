from django.db import models

# Create your models here.
class Character(models.Model):
  ALIGNMENTS = (
    ('E', 'Evil'),
    ('N', 'Neutral'),
    ('G', 'Good'),
  )
  name = models.CharField(max_length=255)
  alignment = models.CharField(max_length=1, choices=ALIGNMENTS, default='N')

class Scenario(models.Model):
  name = models.CharField(max_length=255)
  description = models.CharField(max_length=255)

class Choice(models.Model):
  name = models.CharField(max_length=255)
  type = models.CharField(max_length=255)

class Outcome(models.Model):
  name = models.CharField(max_length=255)
  type = models.CharField(max_length=255)