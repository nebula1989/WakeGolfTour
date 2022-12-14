# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from operator import itemgetter

from django.db import models
from tournament.models import Tournament, Round
from golf_course.models import GolfCourse


class Golfer(models.Model):
    golfer_id = models.IntegerField(primary_key=True)
    golfer_name = models.TextField()
    golfer_birthdate = models.DateField()
    golfer_city = models.TextField(default="unknown",
                                   blank=True)

    class Meta:
        managed = True
        db_table = 'Golfer'

    def __str__(self):
        return self.golfer_name


class TournGolfer(models.Model):
    tg_id = models.IntegerField(primary_key=True, blank=True, null=False)
    tg_tourn = models.ForeignKey(Tournament, models.DO_NOTHING, blank=True, null=True)
    tg_golfer = models.ForeignKey(Golfer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TournGolfer'
        verbose_name = "Tournament Golfer"
        verbose_name_plural = "Tournament Golfers"

    def __str__(self):
        return "{} {}".format(self.tg_tourn.tourn_name,
                              self.tg_golfer.golfer_name)

    def getGolferName(self):
        return self.tg_golfer.golfer_name

    def getTournName(self):
        return self.tg_tourn.tourn_name


class GolferRoundScores(models.Model):
    grs_id = models.IntegerField(primary_key=True, blank=True, null=False)
    grs_tourn_golfer = models.ForeignKey(TournGolfer, models.DO_NOTHING, blank=True, null=True)
    grs_round = models.ForeignKey(Round, models.DO_NOTHING, blank=True, null=True)
    grs_total_score = models.IntegerField(blank=True, null=True)
    grs_hole1_score = models.IntegerField(blank=True, null=True)
    grs_hole2_score = models.IntegerField(blank=True, null=True)
    grs_hole3_score = models.IntegerField(blank=True, null=True)
    grs_hole4_score = models.IntegerField(blank=True, null=True)
    grs_hole5_score = models.IntegerField(blank=True, null=True)
    grs_hole6_score = models.IntegerField(blank=True, null=True)
    grs_hole7_score = models.IntegerField(blank=True, null=True)
    grs_hole8_score = models.IntegerField(blank=True, null=True)
    grs_hole9_score = models.IntegerField(blank=True, null=True)
    grs_hole10_score = models.IntegerField(blank=True, null=True)
    grs_hole11_score = models.IntegerField(blank=True, null=True)
    grs_hole12_score = models.IntegerField(blank=True, null=True)
    grs_hole13_score = models.IntegerField(blank=True, null=True)
    grs_hole14_score = models.IntegerField(blank=True, null=True)
    grs_hole15_score = models.IntegerField(blank=True, null=True)
    grs_hole16_score = models.IntegerField(blank=True, null=True)
    grs_hole17_score = models.IntegerField(blank=True, null=True)
    grs_hole18_score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'GolferRoundScores'
        verbose_name = "Golfer Round Scores"
        verbose_name_plural = "Golfers Round Scores"

    def __str__(self):
        return "{} {} {} {}".format(self.grs_tourn_golfer.tg_golfer,
                                    self.grs_tourn_golfer.tg_tourn,
                                    self.grs_round, self.grs_total_score)

    def getTournScores(tourn_id):

        # list to return
        tournament_scores = list()

        # get the list of tourn golfers for this tournament
        # using the filter method of TournGolfer.objects
        # with the tg_tourn equal to the passed in tourn_id

        tourn_golfers = TournGolfer.objects.filter(tg_tourn=tourn_id)

        # loop through the tourngolfer objects,
        # get the golfer name, tournament name
        # (use the helper functions) and the scores for
        # that golfer for each round of the tournament,

        for tourn_golfer in tourn_golfers:
            # clear total score and create new dictionary object

            total_score = 0
            gts = dict()

            # get the golfer name and tournament name
            # using the tourn_golfer key and the helper
            # methods created above

            gts["golfer_name"] = tourn_golfer.getGolferName()
            gts["tournament_name"] = tourn_golfer.getTournName()

            # store the tourn_golfer_id for indexing later
            gts["tourn_golfer_id"] = tourn_golfer.tg_id

            # get the scores for this tourn_golfer from
            # the GolferRoundScores
            scores = GolferRoundScores.objects.filter(
                grs_tourn_golfer=tourn_golfer,
            ).order_by('grs_round')

            # loop through the scores for each round,
            # putting the score in the dict and adding
            # it to the total score for the tournament
            for i in range(1, len(scores) + 1):
                round_score = scores[i - 1].grs_total_score
                gts["round{}_score".format(i)] = round_score
                total_score = total_score + round_score

            # store the total score
            gts["total_score"] = total_score

            # add the dictionary entry to the list
            tournament_scores.append(gts)

        # return the list sorted by "total_score"
        return sorted(tournament_scores,
                      key=itemgetter('total_score'))

    def getTournScoresByGolfer(golfer_id):

        # list to return
        tournament_scores = list()

        # get the list of tourn golfers for this tournament
        # using the filter method of TournGolfer.objects
        # with the tg_tourn equal to the passed in golfer_id

        tourn_golfers = TournGolfer.objects.filter(tg_golfer=golfer_id)

        # loop through the tourngolfer objects,
        # get the golfer name, tournament name
        # (use the helper functions) and the scores for
        # that golfer for each round of the tournament,

        for tourn_golfer in tourn_golfers:
            # clear total score and create new dictionary object

            total_score = 0
            gts = dict()

            # get the golfer name and tournament name
            # using the tourn_golfer key and the helper
            # methods created above

            gts["golfer_name"] = tourn_golfer.getGolferName()
            gts["tournament_name"] = tourn_golfer.getTournName()

            # store the tourn_golfer_id for indexing later
            gts["tourn_golfer_id"] = tourn_golfer.tg_id

            # get the scores for this tourn_golfer from
            # the GolferRoundScores
            scores = GolferRoundScores.objects.filter(
                grs_tourn_golfer=tourn_golfer,
            ).order_by('grs_round')

            # loop through the scores for each round,
            # putting the score in the dict and adding
            # it to the total score for the tournament
            for i in range(1, len(scores) + 1):
                round_score = scores[i - 1].grs_total_score
                gts["round{}_score".format(i)] = round_score
                total_score = total_score + round_score

            # store the total score
            gts["total_score"] = total_score

            # add the dictionary entry to the list
            tournament_scores.append(gts)

        # return the list sorted by "total_score"
        return sorted(tournament_scores,
                      key=itemgetter('total_score'))

    def getParDiffs(self):
        golfer_scores = []
        for i in range(0, 17):
            score = getattr(self, 'grs_hole{}_score'.format(i + 1))
            golfer_scores.append(score)

        parList = self.grs_tourn_golfer.tg_tourn.tourn_course.getParList()
        round_scores_diff = []
        for i in range(0, 17):
            hole_score_par_diff = []
            hole_score = golfer_scores[i]
            hole_par = parList[i]
            par_diff = hole_score - hole_par

            hole_score_par_diff.append(hole_score)
            hole_score_par_diff.append(par_diff)

            round_scores_diff.append(hole_score_par_diff)

        return round_scores_diff















