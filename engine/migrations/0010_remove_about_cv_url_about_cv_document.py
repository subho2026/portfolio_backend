# Generated by Django 4.2.5 on 2023-09-19 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0009_rename_skills_skill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='cv_url',
        ),
        migrations.AddField(
            model_name='about',
            name='cv_document',
            field=models.FileField(blank=True, null=True, upload_to='cv_documents/'),
        ),
    ]
