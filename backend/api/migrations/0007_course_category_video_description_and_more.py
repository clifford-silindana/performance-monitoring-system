# Generated by Django 5.0.3 on 2024-03-27 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_employee_date_of_hire'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.RemoveField(
            model_name='course',
            name='videos',
        ),
        migrations.AddField(
            model_name='course',
            name='videos',
            field=models.ManyToManyField(blank=True, null=True, to='api.video'),
        ),
    ]
