# Generated by Django 2.2.3 on 2019-10-29 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0005_auto_20190807_2009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=100)),
                ('poster', models.ImageField(upload_to='pics')),
                ('movie_id', models.IntegerField()),
                ('genres', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
