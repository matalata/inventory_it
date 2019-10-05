# Generated by Django 2.1.8 on 2019-10-03 10:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('examples', '0002_auto_20191002_0859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='author',
        ),
        migrations.AddField(
            model_name='equipment',
            name='created_by',
            field=django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='note',
            field=models.CharField(default='', max_length=50, null=True, verbose_name='Примечание'),
        ),
    ]
