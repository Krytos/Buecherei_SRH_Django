# Generated by Django 4.1 on 2022-08-26 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buecherei', '0004_alter_ausleihe_rueckgabedatum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buch',
            name='verlag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='verlag', to='buecherei.verlag'),
        ),
    ]
