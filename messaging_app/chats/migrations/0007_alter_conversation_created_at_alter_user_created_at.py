# Generated by Django 4.2.17 on 2024-12-22 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0006_user_is_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='created_at',
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
