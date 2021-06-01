from django import forms
from .models import Todo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Todocreateform(forms.Form):
    task_name=forms.CharField(max_length=12)
    choices=(("completed","completed"),
             ("notcompleted","notcompleted"))
    status=forms.ChoiceField(choices=choices)
    user=forms.CharField(max_length=12)

    def clean(self):
        pass

class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields=["task_name","status","user"]

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","email","username","password1","password2"]

class Loginform(forms.Form):
    username=forms.CharField(max_length=12)
    password=forms.CharField(max_length=12)