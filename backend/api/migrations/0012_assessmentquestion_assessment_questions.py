# Generated by Django 5.0.3 on 2024-03-29 14:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_department_physical_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssessmentQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='assessment',
            name='questions',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.assessmentquestion'),
        ),
    ]