# Generated by Django 4.2.3 on 2023-11-12 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_author_name_alter_author_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='name',
        ),
    ]
