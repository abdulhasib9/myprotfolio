# Generated by Django 5.0.6 on 2024-05-19 02:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_certification_does_not_expire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='image',
            field=models.ImageField(upload_to='static/education/'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='project',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.project'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='user_profile',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.userprofile'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, upload_to='projects/'),
        ),
    ]
