"""User forms."""
# Django
from django import forms

# Models
from django.contrib.auth.models import User
from users.models import Profile


class SignupForm(forms.ModelForm):
    """Signup form"""

    password_confirm = forms.CharField(
        max_length=70, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password',
                  'first_name', 'last_name', 'email']

    def clean_username(self):
        """username must be unique"""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is alredy use.')

        return username

    def clean(self):
        """Verification password_confirm match"""
        data = super().clean()
        password = data['password']
        password_confirm = data['password_confirm']

        if password != password_confirm:
            raise forms.ValidationError('Passwords do not match.')

        return data

    def save(self):
        data = self.cleaned_data
        data.pop('password_confirm')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()


class ProfileForm(forms.Form):
    """Profile form"""

    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()
