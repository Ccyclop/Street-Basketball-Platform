# Generated by Django 4.0.4 on 2022-06-08 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='users/default-user-avatar.png', upload_to='users'),
        ),
    ]