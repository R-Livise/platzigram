"""Users URLs"""

# Django
from django.urls import path
from django.views.generic import TemplateView

# views
from users import views

urlpatterns = [
    path(
        route='<str:username>/',
        view=TemplateView.as_view(template_name='users/detail'),
        name='detail'
    ),
    path(
        route='login',
        view=views.login_view,
        name='login'
    ),
    path(
        route='logout',
        view=views.logout_view,
        name='logout'
    ),
    path(
        route='signup',
        view=views.signup_view,
        name='signup'
    ),
    path(
        route='me/profile',
        view=views.update_profile,
        name='update_profile'
    ),
]
