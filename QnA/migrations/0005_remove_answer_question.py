# Generated by Django 3.1.2 on 2020-11-09 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QnA', '0004_delete_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
    ]
