# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from golf_course.models import GolfCourse


class Tournament(models.Model):
    tourn_id = models.IntegerField(primary_key=True)
    tourn_name = models.TextField(blank=True, null=True)
    tourn_course = models.ForeignKey(GolfCourse, models.DO_NOTHING, blank=True, null=True)
    tourn_start_date = models.DateField(blank=True, null=True)
    tourn_num_rounds = models.IntegerField(blank=True, null=True)
    tourn_num_golfers = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Tournament'

    def __str__(self):
        return self.tourn_name


class Round(models.Model):
    round_id = models.IntegerField(primary_key=True)
    round_tourn = models.ForeignKey(Tournament, models.DO_NOTHING, blank=True, null=True)
    round_day = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Round'

    def __str__(self):
        return "{}".format(self.round_day)

