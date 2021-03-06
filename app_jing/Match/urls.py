from django.urls import path
from django.views.generic import TemplateView

from Match.views import MatchView, MatchDeleteView, MatchStartView
from Match.views import MatchFinishView, MatchCloseView, MatchResultsView
from Match.views import MatchCommentView

app_name = 'match'

urlpatterns = [
    path('', MatchView.as_view(), name='matches-section'),
    path('create', MatchView.as_view(), name='create'),
    path('delete', MatchDeleteView.as_view(), name='delete'),
    path('start', MatchStartView.as_view(), name='start'),
    path('finish', MatchFinishView.as_view(), name='finish'),
    path('close', MatchCloseView.as_view(), name='close'),
    path('results', MatchResultsView.as_view(), name='results'),
    path('comment', MatchCommentView.as_view(), name='comment'),
]
