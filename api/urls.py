from django.urls import path
from . import views

urlpatterns = [
    path("country", views.CountryList.as_view()),
]
