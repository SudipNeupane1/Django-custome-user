


from django.db import models

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from datetime import datetime


from phonenumber_field.modelfields import PhoneNumberField


class AuthorManager(BaseUserManager):
    def create_user(self,email,phone_number,password=None, **extra_fields ):
        """
        Cerate and save a User with the given phone and passowrd.
        """
        if not email:
            raise ValueError('Users must hava an email address')
        # if not phone_number:
        #     raise ValueError('User must have phone number')

        email = self.normalize_email(email)
    
        user = self.model(email=email, **extra_fields)
        user=self.model(phone_number=phone_number,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_staffuser(self,email,phone_number,password,**extra_fields):
        user = self.create_user(
            email,
            password=password,
            phone_number=phone_number,

        )
        user.staff = True
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,phone_number,password,name):
        user = self.create_user(
            email=email,
            password=password,
            phone_number=phone_number,
            name=name,

        )
        
        user.staff=True
        user.admin=True
        user.save(using=self._db)
        return user



class Author(AbstractBaseUser):
    
    name=models.CharField(max_length=255)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
    )
    phone_number = PhoneNumberField(unique=True)
    is_active= models.BooleanField(default=True)
    staff=models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS=['email','name']

    objects = AuthorManager()
     
       

    def get_full_name(self):
        return self.email

    def __str__(self):
        return self.name
    def has_perm(self,perm,obj=None):
        "Does the user hava a specific permission?"
        return True

    def has_module_perms(self,app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff
    @property
    def is_admin(self):
        "Is the user a admin memeber?"
        return self.admin

  

