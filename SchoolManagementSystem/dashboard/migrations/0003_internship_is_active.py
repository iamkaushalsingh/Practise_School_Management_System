# Generated by Django 5.0.3 on 2024-04-02 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_internship_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='internship',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
