# Generated by Django 2.1.2 on 2019-11-12 18:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UPLOAD', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Answer_key', models.FileField(blank=True, default='Null', help_text='Upload Answer_key ', null=True, upload_to='UPLOAD/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['', 'pdf'])])),
            ],
        ),
    ]
