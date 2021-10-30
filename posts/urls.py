"""Post URLs"""

# Django
from django.urls import path

# Views
from posts import views

urlpatterns = [
    path(
        route='',
        view=views.PostsFeedView.as_view(),
        name='feed'
    ),
    path(
        route='posts/<int:pk>',
        view=views.PostDetailView.as_view(),
        name='detail'
    ),
    path(
        route='post/create/',
        view=views.PostCreateView.as_view(),
        name='create'
    ),
]
