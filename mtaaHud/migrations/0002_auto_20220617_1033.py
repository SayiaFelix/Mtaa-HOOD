# Generated by Django 3.2 on 2022-06-17 07:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mtaaHud', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='neighbourhood',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='p_photo',
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(null=True, upload_to='profiles/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(max_length=240, null=True),
        ),
    ]
