# Generated by Django 4.1.1 on 2022-11-11 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='correspondencia',
            name='Estado',
            field=models.CharField(choices=[('GOOD', 'Buen estado'), ('MID', 'Estado aceptable'), ('BAD', 'Mal estado')], default='GOOD', max_length=4),
        ),
    ]
