from django.urls import path

from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("music", views.music, name="music" ),
  path("terms", views.terms, name="terms"),
  path("index2", views.index2, name="index2"),
  path("logout", views.logout, name="logout"),
  path("comments", views.comments, name="comments")
]