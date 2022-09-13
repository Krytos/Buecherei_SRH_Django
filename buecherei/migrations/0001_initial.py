# Generated by Django 4.1 on 2022-08-26 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vorname', models.CharField(max_length=64)),
                ('nachname', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Bibliotheksbenutzer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('nachname', models.CharField(max_length=64)),
                ('strasse', models.CharField(max_length=64)),
                ('plz', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Verlag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('telefonnummer', models.CharField(max_length=64)),
                ('strasse', models.CharField(max_length=64)),
                ('plz', models.IntegerField()),
                ('ort', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Buch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.IntegerField()),
                ('titel', models.CharField(max_length=64)),
                ('genre', models.CharField(max_length=64)),
                ('jahr', models.IntegerField()),
                ('autorid', models.ManyToManyField(to='buecherei.autor')),
                ('verlagID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buecherei.verlag')),
            ],
        ),
        migrations.CreateModel(
            name='Ausleihe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frist', models.IntegerField()),
                ('ausleihdatum', models.DateField()),
                ('rueckgabedatum', models.DateField()),
                ('bibliotheksbenutzerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buecherei.bibliotheksbenutzer')),
                ('buchID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buecherei.buch')),
            ],
        ),
    ]