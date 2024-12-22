from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
import uuid

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("Email must be filled")
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_super_user(self, email, password=None, **kwargs):
        kwargs.setdefault('Is_staff', True)
        kwargs.setdefault('Is_superuser', True)
        return self.create_super_user(email, password, **kwargs)
    
class user(AbstractBaseUser):
    '''
        Creating Abstract User Model for the following attributes
            User
        user_id (Primary Key, UUID, Indexed)
        first_name (VARCHAR, NOT NULL)
        last_name (VARCHAR, NOT NULL)
        email (VARCHAR, UNIQUE, NOT NULL)
        password_hash (VARCHAR, NOT NULL)
        phone_number (VARCHAR, NULL)
        role (ENUM: 'guest', 'host', 'admin', NOT NULL)
        created_at (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)
        '''

    role_choices = [
        ('guest','guest'),
        ('host', 'host'),
        ('admin', 'admin')
        ]
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    role = models.CharField(
        max_length=10,
        choices=role_choices,
        default='guest'
    )
    created_at = models.TimeField(auto_created=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
        'phone_number',
        'role'
    ]


class Conversation(models.Model):

    '''
            Conversation
        conversation_id (Primary Key, UUID, Indexed)
        participants_id (Foreign Key, references User(user_id)
        created_at (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)
    '''
    conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    participants_id = models.ForeignKey(user, on_delete=models.DO_NOTHING ,null=True)
    created_at = models.TimeField(auto_created=True)
    

class Message(models.Model):
    '''
            Message
    message_id (Primary Key, UUID, Indexed)
    sender_id (Foreign Key, references User(user_id))
    message_body (TEXT, NOT NULL)
    sent_at (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)
    
    '''
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender_id = models.ForeignKey(user, on_delete=models.CASCADE, null=False)
    sent_at = models.TimeField(auto_created=True)
