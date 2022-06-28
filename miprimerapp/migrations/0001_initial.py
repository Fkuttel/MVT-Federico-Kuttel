# Generated by Django 4.0.5 on 2022-06-27 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='familiares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('altura', models.IntegerField()),
                ('fecha_de_nacimiento', models.DateField(null=True)),
            ],
        ),
    ]
