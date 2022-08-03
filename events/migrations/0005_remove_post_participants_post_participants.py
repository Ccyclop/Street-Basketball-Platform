# Generated by Django 4.0.4 on 2022-06-09 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_initial'),
        ('events', '0004_alter_post_participants'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='participants',
        ),
        migrations.AddField(
            model_name='post',
            name='participants',
            field=models.ManyToManyField(blank=True, to='teams.team'),
        ),
    ]