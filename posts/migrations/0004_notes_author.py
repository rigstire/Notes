# Generated by Django 3.2.4 on 2021-08-16 20:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_remove_notes_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='author',
            field=models.ForeignKey(blank=True, default=5, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
