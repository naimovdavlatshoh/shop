from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    password1 = forms.CharField(
        label='Пароль', 
        min_length=8, 
        required=True, 
        widget=forms.PasswordInput(attrs={'placeholder': '', 'class':'input input-md'}))

    password2 = forms.CharField(
        label='Повторите пароль', 
        min_length=8, 
        required=True, 
        widget=forms.PasswordInput(attrs={'placeholder': '', 'class':'input input-md'}),
        help_text='Enter the same password as before, for verification.',
        )

    email = forms.EmailField(
        label='Email', 
        required=True, 
        widget=forms.TextInput(attrs={'placeholder': '', 'class':'input input-md'}))
     

    class Meta:
        model = CustomUser
        fields = ('email',)


    def save(self, commit=True):
        user = CustomUser.objects.create_user(
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user    
  

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = CustomUser.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email


    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)