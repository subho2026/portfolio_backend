# Generated by Django 4.2.5 on 2023-09-18 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0004_alter_professionalexperience_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='degree',
            field=models.CharField(default='M.Sc Artifical Intelligence', max_length=1024),
            preserve_default=False,
        ),
    ]
