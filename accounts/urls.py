from django.urls import path
from .views import *



urlpatterns = [
    path('resume/', FormView.as_view(), name='resume'),
    path('profile', Profile.as_view(), name='profile'),
    path('<pk>/', ResumeFormView.as_view()),
    path('<pk>/delete/', ResumeFormDelete.as_view()),

] 
