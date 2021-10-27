"""Users views."""

# Django
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Excepts
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from users.models import Profile


def update_profile(request):
    profile = request.user.profile

    return render(request,
                  'users/update_profile.html',
                  context={
                      'user': request.user,
                      'profile': profile
                  }
                  )


def login_view(request):
    """Login view."""
    print(request.method)
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('feed')
        else:
            return render(request,
                          'users/login.html',
                          {'error': 'Invalid username and password'}
                          )

    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    """Logout view."""
    logout(request)
    return redirect('login')


def signup_view(request):
    """Signup view."""
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        password_confirm = request.POST["password_confirm"]
        if password != password_confirm:
            return render(request, 'users/signup.html', {'error': 'Password confirm does not math'})
        try:
            user = User.objects.create_user(
                username=username, password=password)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Username is already in used'})

        user.first_name = request.POST["first_name"]
        user.last_name = request.POST["last_name"]
        user.email = request.POST["email"]
        profile = Profile(user=user)
        profile.save()

        return redirect('login')

    return render(request, 'users/signup.html')
