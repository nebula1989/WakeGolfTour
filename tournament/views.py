from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Tournament
from golfer.models import GolferRoundScores


# list tournaments from home page hyperlinks
class TournamentListView(generic.ListView):
    model = Tournament
    template_name = 'tournament/tournament_list.html'
    context_object_name = 'tournaments'


class TournamentDetailView(generic.DetailView):
    model = Tournament
    template_name = 'tournament/tournament_detail.html'

    # we need to override get_context_data
    def get_context_data(self, **kwargs):
        # get context dictionary
        context = super(TournamentDetailView, self).get_context_data(**kwargs)

        # we are using tourn object which was clicked by user
        tournament = self.get_object()

        # use tourn object to get rest of context
        context['tournament'] = tournament
        # call GolferRoundScores method, getTournScores, to return scores
        context['scores'] = GolferRoundScores.getTournScores(tournament.tourn_id)

        return context
