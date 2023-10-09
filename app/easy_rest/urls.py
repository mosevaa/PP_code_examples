from django.urls import path

from .views import UserInfoView


app_name = "articles"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('', UserInfoView.as_view()),
]