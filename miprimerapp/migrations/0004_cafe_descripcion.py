# Generated by Django 4.0.5 on 2022-08-19 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miprimerapp', '0003_delete_te'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafe',
            name='descripcion',
            field=models.TextField(null=True),
        ),
    ]
