# Generated by Django 4.0.5 on 2022-08-02 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Te',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=30)),
                ('aroma', models.CharField(blank=True, max_length=30)),
            ],
        ),
    ]
