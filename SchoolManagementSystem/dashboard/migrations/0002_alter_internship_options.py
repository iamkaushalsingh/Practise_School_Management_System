# Generated by Django 5.0.3 on 2024-04-02 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='internship',
            options={'permissions': [('can_post_internship', 'Can post internship'), ('can_edit_internship', 'Can edit internships'), ('can_delete_internship', 'Can delete internships'), ('can_apply_to_internship', 'Can apply to internships'), ('can_view_applied_internships', 'Can view all applied internships'), ('can_view_internship_applications', 'Can view all applications to internships')]},
        ),
    ]
