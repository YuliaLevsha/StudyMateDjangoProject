# Generated by Django 4.2.2 on 2023-06-21 08:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('EduNova', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('32465990-4f5a-4057-b35a-48f4e77a32e7'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='goal',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('6a31f70b-2c9d-4445-b3ed-8096f3c2c2fe'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='note',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('9faacc0d-cecf-4ae5-96cd-04dd25c9611c'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='topic',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('7a945c63-59ec-49b1-bbeb-d4a7ce1eeaab'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('e7009b1c-898b-4778-ad08-f93849d352ba'), editable=False, primary_key=True, serialize=False),
        ),
    ]