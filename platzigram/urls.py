"""Modulo de urls django"""
# Django
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from platzigram import views as local_views
from posts import views as posts_views
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-word/', local_views.hello_world, name="hello_word"),
    path('sorted/', local_views.sort_integers, name="sort"),
    path('hi/<str:name>/<int:age>', local_views.say_hi, name="hi"),

    path('users/login', users_views.login_view, name="login"),
    path('users/logout', users_views.logout_view, name="logout"),
    path('users/signup', users_views.signup_view, name="signup"),
    path('users/me/profile', users_views.update_profile, name="update_profile"),

    path('posts/', posts_views.list_posts, name="feed")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
