# Generated by Django 2.0.7 on 2018-08-07 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_auto_20180807_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highscore',
            name='besttime',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='highscore',
            name='username',
            field=models.CharField(max_length=200),
        ),
    ]
