# Generated by Django 2.2.7 on 2019-12-29 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0002_auto_20191213_0249'),
    ]

    operations = [
        migrations.AddField(
            model_name='techskill',
            name='rating',
            field=models.IntegerField(default=1),
        ),
    ]