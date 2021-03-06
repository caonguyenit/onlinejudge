# Generated by Django 2.2.24 on 2021-11-18 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0165_contest_show_submission_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='scoreboard_cache_timeout',
            field=models.PositiveIntegerField(default=0, help_text='How long should the scoreboard be cached. Set to 0 to disable caching.', verbose_name='scoreboard cache timeout'),
        ),
    ]
