# Generated by Django 3.2.10 on 2022-02-28 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('searched', models.TextField()),
                ('time_searched', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
