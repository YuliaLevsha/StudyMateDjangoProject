# Generated by Django 4.2.2 on 2023-06-21 08:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('uuid', models.UUIDField(default=uuid.UUID('69a7db2a-c248-4027-87d3-2a9843821862'), editable=False, primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('header', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('uuid', models.UUIDField(default=uuid.UUID('e7e8aec3-5f49-4cf2-9526-a5b7d3b59c2f'), editable=False, primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=33)),
                ('email', models.EmailField(max_length=25, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('uuid', models.UUIDField(default=uuid.UUID('b9470ea4-cd0b-4d07-b322-80d51a7ffd09'), editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('percent', models.DecimalField(decimal_places=2, max_digits=5)),
                ('uuid_user', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('topics', models.ManyToManyField(to='EduNova.topic')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('uuid', models.UUIDField(default=uuid.UUID('20d7dacb-2430-4cce-9dcd-789eef343725'), editable=False, primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('uuid_article', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='EduNova.article')),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('uuid', models.UUIDField(default=uuid.UUID('6ce568c5-e047-4526-a6a5-68770de83738'), editable=False, primary_key=True, serialize=False)),
                ('task', models.CharField(max_length=50)),
                ('status', models.BooleanField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('uuid_topic', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='EduNova.topic')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='uuid_topic',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='EduNova.topic'),
        ),
    ]