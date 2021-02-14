from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from avalita.models import allowed_emails


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, help_text='Required. 30 characters or fewer.')
    last_name = forms.CharField(max_length=30, help_text='Required. 30 characters or fewer.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    def clean_email(self):
        email = self.cleaned_data['email']
        registered_emails = [u.email for u in User.objects.all()]
        if email in registered_emails:
            raise forms.ValidationError("A user with that email address already exists")
        if not any([email.endswith(e) for e in allowed_emails]):
            raise forms.ValidationError("Must be a @ga.ita.br or @gp.ita.br address")
        return email

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
