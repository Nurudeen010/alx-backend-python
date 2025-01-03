# Generated by Django 4.2.17 on 2024-12-31 15:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0010_alter_message_sender_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='conversation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='chats.conversation'),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='participants_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='conversations', to=settings.AUTH_USER_MODEL),
        ),
    ]
