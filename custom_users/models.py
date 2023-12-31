from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group

class MyAccountManager(BaseUserManager):
    def create_user(self, email,username,first_name,last_name, password=None):
        """
        Creates and saves a User with the given email, username,
        first_name,last_name and password.
        """
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a user name")
        if not first_name:
            raise ValueError("Users must have a first name")
        if not last_name:
            raise ValueError("Users must have a last name")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,username,first_name,last_name, password):
        """
        Creates and saves a User with the given email, username,
        first_name,last_name and password.
        """
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
           
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(verbose_name="last login",auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']
    
    objects = MyAccountManager()
    
    def __str__(self):
        return self.username
    def has_perm(self, perm,obj=None):
        return self.is_admin 
    def has_module_perms(self, app_label):
        return True 
        
@receiver(post_migrate)
def create_default_roles(sender, **kwargs):
    if sender.name == 'custom_users':
        # Replace 'myapp' with the actual name of your app
        Group.objects.get_or_create(name='Admin')
        Group.objects.get_or_create(name='Biller')
        Group.objects.get_or_create(name='Customer')
        Account.objects.create_superuser('admin@kacha.et','test','Kaleb'
                                         ,'Takele','Test1324!')

