import uuid

from django.core.cache import cache
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models import F
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from EduNova.forms import *


def main_page(request):
    context = None
    if request.user.is_authenticated:
        context = logout_page
    return render(request, 'EduNova/index.html', {'context': context})


def register_page(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Аккаунт был создан для ' + user)
            return redirect('login')
    return render(request, 'EduNova/register.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Пароль неверный или имя пользователя')
    return render(request, 'EduNova/login.html')


@login_required(login_url='login')
def logout_page(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def addtopic_page(request):
    if request.method == 'POST':
        form = AddTopicForm(request.POST)
        form2 = AddArticleForm(request.POST)
        if form.is_valid() and form2.is_valid():
            topic = form.save(commit=False)
            article = form2.save(commit=False)

            topic.uuid = uuid.uuid4()
            article.uuid = uuid.uuid4()

            topic.uuid_user = request.user
            article.uuid_topic = topic
            article.head = True

            topic.save()
            article.save()
            return redirect('home')
    else:
        form = AddTopicForm()
        form2 = AddArticleForm()
    return render(request, 'EduNova/addtopic.html', {'form': form, 'form2': form2})


def get_list_topic(request):
    list_all = Article.objects.select_related('uuid_topic').filter(head=True)
    return render(request, 'EduNova/list_topic.html', {'list_all': list_all})


def get_one_page(request, topic_uuid):
    topic = Topic.objects.get(uuid=topic_uuid)
    note = Note.objects.select_related('uuid_article').filter(uuid_article__uuid_topic=topic_uuid)
    goal = Goal.objects.filter(uuid_topic=topic_uuid)

    list_article = []
    article = Article.objects.select_related('next_article').filter(uuid_topic=topic_uuid)
    current_article = Article.objects.select_related('next_article').get(uuid_topic=topic_uuid, head=True)
    while current_article:
        for a in article:
            if a == current_article:
                list_article.append(a)
                current_article = a.next_article
                break

    value = 0.0
    if goal:
        all_goals = 0
        count_true = 0
        for g in goal:
            if g.status:
                count_true += 1
            all_goals += 1
        value = "{:.2f}".format(float(count_true / all_goals * 100))
        topic.percent = value
        topic.save()

    if request.method == 'POST':
        list_uuid_checked = request.POST.getlist('goal')
        for g in goal:
            if str(g.uuid) in list_uuid_checked:
                g.status = True
                g.save()

        form = AddNoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.uuid = uuid.uuid4()
            article_uuid = request.POST.get('article_uuid')
            article = Article.objects.get(uuid=article_uuid)
            note.uuid_article = article
            note.save()
        return redirect(f'http://127.0.0.1:8000/list_topic/{topic_uuid}/')
    else:
        form = AddNoteForm()
    return render(request, 'EduNova/topic.html', {'list_article': list_article, 'note': note, 'form': form,
                                                  'goal': goal, 'topic': topic})


@login_required(login_url='login')
def add_article(request, topic_uuid):
    if request.method == 'POST':
        previous_uuid = request.GET.get('add')
        form = AddArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)

            article.uuid = uuid.uuid4()
            topic = Topic.objects.get(uuid=topic_uuid)
            article.uuid_topic = topic

            article.save()
            next_ = None

            if previous_uuid:
                prev_article = Article.objects.get(uuid=previous_uuid)
                next_ = prev_article.next_article
                prev_article.next_article = article
            else:
                prev_article = Article.objects.get(uuid_topic=topic_uuid, head=True)
                next_ = prev_article
                prev_article.head = False
                article.head = True

            article.next_article = next_

            prev_article.save()
            article.save()
            return redirect(f'http://127.0.0.1:8000/list_topic/{topic_uuid}/')
    else:
        form = AddArticleForm()
    return render(request, 'EduNova/add_article.html', {'form': form})


@login_required(login_url='login')
def add_goal(request, topic_uuid):
    if request.method == 'POST':
        form = AddGoals(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)

            goal.uuid = uuid.uuid4()
            topic = Topic.objects.get(uuid=topic_uuid)
            goal.uuid_topic = topic

            goal.save()
            return redirect(f'http://127.0.0.1:8000/list_topic/{topic_uuid}/')
    else:
        form = AddGoals()
    return render(request, 'EduNova/add_goal.html', {'form': form})
