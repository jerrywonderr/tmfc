# Generated by Django 3.1.5 on 2021-12-26 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='text',
            new_name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='blocked',
            field=models.BooleanField(default=True),
        ),
    ]
