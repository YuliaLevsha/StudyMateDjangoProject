import uuid as uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    login = models.CharField(max_length=15)
    password = models.CharField(max_length=33)
    email = models.EmailField(max_length=25, unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Topic(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=50)
    percent = models.DecimalField(max_digits=5, decimal_places=2)
    uuid_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default=None)


class Goal(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    task = models.CharField(max_length=50)
    status = models.BooleanField()
    value = models.DecimalField(max_digits=5, decimal_places=2)
    uuid_topic = models.ForeignKey(Topic, on_delete=models.CASCADE, blank=True, default=None)


class Article(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    text = models.TextField()
    header = models.CharField(max_length=30)
    uuid_topic = models.ForeignKey(Topic, on_delete=models.CASCADE, blank=True, default=None)


class Note(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    text = models.TextField()
    uuid_article = models.ForeignKey(Article, on_delete=models.CASCADE, blank=True, default=None)


class Tag(models.Model):
    name = models.CharField(max_length=30)
    topics = models.ManyToManyField(Topic)
