# Generated by Django 3.1.4 on 2021-05-03 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PredResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Patient_ID', models.IntegerField()),
                ('Patient_Age', models.IntegerField()),
                ('Patient_Gender', models.IntegerField()),
                ('Heart_Disease', models.CharField(max_length=30)),
            ],
        ),
    ]
