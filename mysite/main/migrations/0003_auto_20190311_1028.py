# Generated by Django 2.1.7 on 2019-03-11 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_myfile_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='myfile',
            name='owner',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='myfile',
            name='file',
            field=models.FileField(upload_to='media'),
        ),
    ]
