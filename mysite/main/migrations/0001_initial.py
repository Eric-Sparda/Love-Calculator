# Generated by Django 4.2.4 on 2023-08-07 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoveCalculator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person1_name', models.CharField(max_length=100)),
                ('person2_name', models.CharField(max_length=100)),
                ('love_percentage', models.IntegerField(default=0)),
            ],
        ),
    ]
