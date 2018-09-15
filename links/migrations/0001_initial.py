# Generated by Django 2.1.1 on 2018-09-14 16:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Headline')),
                ('submitted_on', models.DateTimeField(auto_now_add=True)),
                ('rank_score', models.FloatField(default=0.0)),
                ('url', models.URLField(blank=True, max_length=250, verbose_name='URL')),
                ('description', models.TextField(blank=True)),
                ('submitter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='links.Link')),
                ('voter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
