# Generated by Django 5.0.3 on 2024-03-28 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_video_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='physical_address',
            field=models.TextField(),
        ),
    ]
