from django.urls import path
from . import views

urlpatterns = [
    path("people", views.PersonList.as_view()),
    path("country", views.CountryList.as_view()),
]
