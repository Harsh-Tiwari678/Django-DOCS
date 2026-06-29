
from django.urls import path
from . import views # hamari current directiry mein se import kar lijiye views ko 

urlpatterns = [
    path('' , views.app , name="basicApp")
]