# Generated by Django 3.0.7 on 2020-07-07 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('werewolf', '0002_werewolf_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='werewolf',
            name='slug',
            field=models.SlugField(default='hello-world'),
            preserve_default=False,
        ),
    ]
