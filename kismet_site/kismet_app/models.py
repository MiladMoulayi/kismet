from django.db import models

# Create your models here.

# Character model with attributes name and alignment.
# Name is a simple character field and alignment is a character field which selects from predefined choices ==> ALIGNMENTS.
class Character(models.Model):
  ALIGNMENTS = (
    ('E', 'Evil'),
    ('N', 'Neutral'),
    ('G', 'Good'),
  )
  name = models.CharField(max_length=255)
  alignment = models.CharField(max_length=1, choices=ALIGNMENTS, default='N')

# Scenario model with attributes name and description.
# Both name and destrictipn are simple character fields.
class Scenario(models.Model):
  name = models.CharField(max_length=255)
  description = models.CharField(max_length=255)

  def __str__(self):
      return self.name

# Choice model with attributes name, type, the_scenario, and level.
# Name and type are simple character fields. name is the description of the choice, and type is
# the moral alignment of the choice. the_scenario is a foreign key field that defines a many-to-one
# relationship between the choice and a scenario. level is a positive small integer field that
# defines how many steps into the scenario or 'path' the player is for the purposes of keeping
# track of what choices are available to him at what point in the 'path'.
class Choice(models.Model):
  name = models.CharField(max_length=255)
  type = models.CharField(max_length=255)
  the_scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE, null=True, blank=True)
  level = models.PositiveSmallIntegerField(default=0)

# Outcome model with attributes name, type, choices, scenario, and level.
# Like above, name and type are simple character fields representing the description of the outcome
# and the moral alignment respectively. choices is a many-to-many field defining what choices
# are available within the scope of this outcome. scenario is as above a foreign key field that
# defines a many-to-one relationship between the outcome and the scenario, and level functions
# as above by keeping track of how many steps into the path the player is.
class Outcome(models.Model):
  name = models.CharField(max_length=255)
  type = models.CharField(max_length=255)
  choices = models.ManyToManyField(Choice)
  scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE, null=True, blank=True)
  level = models.PositiveSmallIntegerField(default=0)