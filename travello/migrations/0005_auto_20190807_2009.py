# Generated by Django 2.2.3 on 2019-08-07 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0004_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratings',
            name='movie_id',
            field=models.CharField(max_length=100),
        ),
    ]