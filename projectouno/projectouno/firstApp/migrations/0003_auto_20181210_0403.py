# Generated by Django 2.1.4 on 2018-12-10 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0002_lesson'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='lesson',
            name='content',
            field=models.TextField(blank=True, default=''),
        ),
    ]
