# Generated by Django 4.2.5 on 2023-09-13 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0003_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professionalexperience',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='professionalexperience',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files'),
        ),
        migrations.AlterField(
            model_name='project',
            name='demo_url',
            field=models.URLField(blank=True),
        ),
    ]
