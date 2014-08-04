from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

__author__ = 'ayomidebell'

class SnakeUserCreationForm(UserCreationForm):
        email = forms.EmailField(required=True)
        # first_name = forms.CharField(max_length=100)
        # last_name = forms.CharField(max_length=100)
        # avatar = forms.ImageField(required=True)
        # bio = forms.CharField(max_length=150, widget=forms.Textarea(attrs={'placeholder': 'Tell us about yourself'}))

        class Meta:
            model = User
            fields = ("username", "email", "password1",
                      "password2")
        #
        # def clean_username(self):
        #     # Since User.username is unique, this check is redundant,
        #     # but it sets a nicer error message than the ORM. See #13147.
        #     username = self.cleaned_data["username"]
        #     try:
        #         SkateUser.objects.get(username=username)
        #     except SkateUser.DoesNotExist:
        #         return username
        #     raise forms.ValidationError(
        #         self.error_messages['duplicate_username'],
        #         code='duplicate_username',
        #     )
