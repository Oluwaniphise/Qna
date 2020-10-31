from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('details/<slug>/', views.question_details, name="question_details"),
    path('ask/', views.ask, name="ask")
]
