# Generated by Django 4.0.3 on 2022-03-18 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tpvapp', '0002_depence_date_depence_montant'),
    ]

    operations = [
        migrations.CreateModel(
            name='recette',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.FloatField(default=0)),
                ('date', models.DateField(default=None)),
            ],
        ),
    ]