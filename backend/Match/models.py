from django.db import models

from Event.models import Event
from Location.models import Location
from Team.models import Team
from Sport.models import Sport


class Match(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    date = models.DateTimeField()
    played = models.BooleanField(default=False)
    closed = models.BooleanField(default=False)
    time_finished = models.DateTimeField(null=True, blank=True)
    comment = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        match_teams = self.match_teams.all()
        teams = '-'.join([mt.team.university.short_name for mt in match_teams])
        return '{} ({})'.format(self.sport, teams)
class MatchTeam(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, related_name='match_teams', on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)
    comment = models.TextField(max_length=300, blank=True)
    is_winner = models.BooleanField(default=False)
    attended = models.BooleanField(default=False)

    def __str__(self):
        return str(self.team)
