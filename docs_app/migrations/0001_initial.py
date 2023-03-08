# Generated by Django 4.1.5 on 2023-03-07 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=13)),
                ('given_amt', models.IntegerField(default=0)),
                ('daily_amt', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now_add=True)),
                ('records', models.JSONField()),
            ],
        ),
    ]
