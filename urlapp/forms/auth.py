from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'example@example.com',
    }))
    username = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
    }))
    password = forms.CharField(min_length=6, max_length=255, required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
    }))
    password2 = forms.CharField(min_length=6, max_length=255, required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Repeat password',
    }))

    def clean(self):
        if not self.cleaned_data['password'] == self.cleaned_data['password2'] or not self.cleaned_data['password2']:
            self._errors['password2'] = self.error_class(['Password doesn\'t match'])
        return self.cleaned_data

    def save(self, commit=True):
        return User.objects.create_user(
            email=self.cleaned_data['email'], 
            username=self.cleaned_data['username'], 
            password=self.cleaned_data['password']
            )

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'password2')

class LogInForm(forms.Form):

    username = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
    }))

    password = forms.CharField(min_length=6, max_length=255, required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
    }))