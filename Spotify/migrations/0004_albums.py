# Generated by Django 2.0.6 on 2018-06-09 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Spotify', '0003_genres'),
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('cover', models.TextField()),
                ('artist_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Spotify.Artist')),
                ('genre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Spotify.Genres')),
            ],
        ),
    ]
