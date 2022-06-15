# Generated by Django 3.2.7 on 2021-11-30 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('music', '0001_initial'), ('music', '0002_song_artist_name')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('artist_name', models.CharField(default='unknown', max_length=50)),
            ],
        ),
    ]