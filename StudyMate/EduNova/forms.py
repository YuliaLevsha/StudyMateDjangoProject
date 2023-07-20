from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import *


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AddTopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data['name']
        if str(name).isdigit():
            raise ValidationError('Тема не может состоять только из цифр!')
        return name


class AddArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['text', 'header']


class AddNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['text']


class AddGoals(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['task']


