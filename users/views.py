"""Users views."""

# Django
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.urls import reverse, reverse_lazy

# Models
from django.contrib.auth.models import User
from django.views.generic.edit import FormView, UpdateView
from posts.models import Post

# Forms
from users.forms import SignupForm
from users.models import Profile


class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view."""
    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Ass user's posts to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context


class SignupView(FormView):
    """Sign up view"""
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update a user 's profile view."""
    template_name = 'users/update_profile.html'
    model = Profile
    fields = [
        'website',
        'biography',
        'phone_number',
        'picture',
    ]

    def get_object(self):
        """Return user's profile"""
        return self.request.user.profile

    def get_success_url(self):
        """Return url """
        username = self.request.user.username
        return reverse('users:detail',
                       kwargs={'username': username}
                       )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context


class LoginView(auth_views.LoginView):
    """Login view."""
    template_name = 'users/login.html'


class LogoutView(auth_views.LogoutView):
    """Logout view."""
    template_name = 'users/login.html'

# def update_profile(request):
#     """Update a user 's profile view."""
#     profile = request.user.profile

#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             data = form.cleaned_data
#             profile.website = data['website']
#             profile.biography = data['biography']
#             profile.phone_number = data['phone_number']
#             profile.picture = data['picture']
#             profile.save()
#             print('*'*30, 'condicion')

#             url = reverse('users:detail', kwargs={
#                           'username': request.user.username})
#             return redirect(url)
#     else:
#         form = ProfileForm()

#     return render(request,
#                   'users/update_profile.html',
#                   context={
#                       'user': request.user,
#                       'profile': profile,
#                       'form': form
#                   }
#                   )


# def signup_view(request):
#     """Sign up view"""
#     if request.method == 'POST':
#         form = SignupForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return redirect('users:login')
#     else:
#         form = SignupForm()

#     return render(
#         request=request,
#         template_name='users/signup.html',
#         context={'form': form}
#     )


# def login_view(request):
#     """Login view."""
#     print(request.method)
#     if request.method == "POST":
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('posts:feed')
#         else:
#             return render(request,
#                           'users/login.html',
#                           {'error': 'Invalid username and password'}
#                           )

#     return render(request, 'users/login.html')

# @login_required
# def logout_view(request):
#     """Logout view."""
#     logout(request)
#     return redirect('users:login')
