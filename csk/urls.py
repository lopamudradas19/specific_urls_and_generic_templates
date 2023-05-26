from django.urls import path
from csk.views import*
app_name='game'
urlpatterns=[
    path('msd/',msd,name='msd'),
]