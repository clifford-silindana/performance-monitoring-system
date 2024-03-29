# Generated by Django 5.0.3 on 2024-03-25 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_course_assessments_assessment_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='number_of_students',
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, null=True, to='api.employee'),
        ),
    ]
