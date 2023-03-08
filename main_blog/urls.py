from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # TODO adding optional title to path for showing posts
    path(r"post/<int:post_id>/", views.post_view, name="post_view"),
    path(r"tag/<str:tag_name>/", views.tag_view, name="tag_view"),
    path(r"aboutme/", views.about_me, name="about_me"),
]
