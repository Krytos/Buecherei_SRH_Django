# Generated by Django 4.1 on 2022-08-26 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buecherei', '0008_alter_autor_buch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autor',
            name='buch',
        ),
        migrations.AddField(
            model_name='buch',
            name='autor',
            field=models.ManyToManyField(related_name='autor', to='buecherei.autor'),
        ),
    ]
