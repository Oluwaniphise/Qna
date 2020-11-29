from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('details/<slug>/<int:question_id>/', views.question_details, name="question_details"),
    path('ask/', views.ask, name="ask"),
    path('answer/<slug>/<int:question_id>/', views.answer_form, name="answer-form"),
    path('like/', views.like_question, name="like-question"),
    path('profile/', views.profile, name="profile"),
 
] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)