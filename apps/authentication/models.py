from django.db import models
#to import features we enter the following
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
#Allows us to set the jwt settings
from rest_framework_jwt.settings import api_settings

#checking credentials
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, fullname=None, password=None):
        if email is None:
            raise TypeError('Must enter an email')
        #creating user object
        user = self.model(
            fullname = fullname,
            #check if the email is valid, normalize by lowercasing
            email = self.normalize_email(email),
            #this states that every time a user creates an account they are regular users
            is_staff = False
        )
        #encryption and info been stored in db
        user.set_password(password)
        user.save()

        return user

    #creating a super-user
    def create_superuser(self, email, password):
        if password is None:
            raise TypeError ("Must have a password")
        user = self.create_superuser(email, password)
        user.is_superuser=True
        user.is_staff=True
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(db_index=True,unique=True)
    fullname = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    #this will need to be change to false / later on
    is_staff = models.BooleanField(default=True)
    #creating a permanent record for new user
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['email']

    #User manger defined above should manage objects of this type
    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        payload = jwt_encode_handler(self)
        token = jwt_payload_handler(payload)

        return token