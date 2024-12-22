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
    
    def create_superuser(self, email, password=None, **kwargs):
        # Set is_staff and is_superuser to True for superusers
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)

        # Ensure superuser requirements are met
        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        # Call the create_user method to create the superuser
        return self.create_user(email, password, **kwargs)
    
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
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=15)
    role = models.CharField(
        max_length=10,
        choices=role_choices,
        default='guest'
    )
    created_at = models.TimeField(auto_now_add=True)

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
    created_at = models.TimeField(auto_now_add=True)
    

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
    message_body = models.TextField(null=False, default='Your message here')
    sent_at = models.TimeField(auto_created=True)