import uuid as uuid

from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, UserManager
from django.db import models


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('-----')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4())
    username = models.CharField(max_length=15)
    email = models.EmailField(max_length=25, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Topic(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=50)
    percent = models.FloatField(default=0.0)
    uuid_user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)


class Goal(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    task = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    uuid_topic = models.ForeignKey(Topic, on_delete=models.CASCADE, blank=True, default=None)


class Article(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4())
    text = models.TextField()
    header = models.CharField(max_length=30)
    uuid_topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=False)
    next_article = models.OneToOneField('self', on_delete=models.SET_NULL, default=None, null=True)
    head = models.BooleanField(default=False)


class Note(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    text = models.TextField()
    uuid_article = models.ForeignKey(Article, on_delete=models.CASCADE, blank=True, default=None)


class Tag(models.Model):
    name = models.CharField(max_length=30)
    topics = models.ManyToManyField(Topic)
