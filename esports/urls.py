from django.urls import path 
from django.conf.urls import handler404
from . import views

app_name = 'esports'

urlpatterns = [
    path('league-of-legends/', views.league_of_legends, name='league-of-legends' ),
]


