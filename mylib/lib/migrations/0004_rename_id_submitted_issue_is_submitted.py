# Generated by Django 4.1 on 2022-08-19 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0003_issue_id_submitted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issue',
            old_name='id_submitted',
            new_name='is_submitted',
        ),
    ]
