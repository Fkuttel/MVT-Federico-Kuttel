# Generated by Django 4.0.5 on 2022-07-07 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miprimerapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='familiares',
        ),
    ]
