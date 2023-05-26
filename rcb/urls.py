from django.urls import path
from rcb.views import*
app_name='hockey'
urlpatterns=[
    path('virat/',virat,name='virat'),
]