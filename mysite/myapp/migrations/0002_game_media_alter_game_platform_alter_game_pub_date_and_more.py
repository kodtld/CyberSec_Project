# Generated by Django 4.1.1 on 2022-10-30 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='media',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='game',
            name='platform',
            field=models.CharField(default='eg. Playstation', max_length=50),
        ),
        migrations.AlterField(
            model_name='game',
            name='pub_date',
            field=models.DateField(default='YYYY-MM-DD', verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='game',
            name='title',
            field=models.CharField(default='Name of release', max_length=200),
        ),
    ]
