from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Create your models here.
class UserProfileManager(BaseUserManager):
    """Super user is being created here and who can see all the data models and the database stuffs and manager for all user profiles"""
    def create_user(self, email, name, password):
        if not email:
           raise ValueError("Email Cannot be blank")
        else:
            email = self.normalize_email(email)
            # now we will create a new model object using 
            user = self.model(email=email,name=name)
            # the password that we get here might be hashed and this method is being called in the create function of the serializer
            # for setting the password for the user object that is being created above
            user.set_password(password)
            # set_password is a method that is being provided by inherited parent class BaseUserManager
            # set_password hashifies the password
            # django supports mulitple database that is why when saving the records to the database we use 
            user.save(using=self._db)
            return user

    def create_superuser(self,email,name,password):
        """create and save the new super user with the following details"""
        user = self.create_user(email, name, password)
        user.is_staff = True
        user.is_superuser = True
        # is_superuser is the method that is provideed by BaseUserManager
        user.save(using=self._db)
        return user    
            

class UserProfile(AbstractBaseUser,PermissionsMixin):
    """"this is for the UserProfile Model"""
    email = models.EmailField(unique=True, max_length=255)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default = False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


    def get_full_name(self):
        """Retrieves the full name from the User record"""
        return self.name

    def get_short_name(self):
        """Retrieves the short name from the User record """
        return self.name
  
    def __str__(self):
        """returns the string representation of the user email"""
        return self.email