from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

from common.models import BaseModel


class AccountManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, password=None):        
        
        if not email :            
            raise ValueError('must have user email')        
        user = self.model(            
            email=self.normalize_email(email),
        )        
        user.set_password(password)        
        user.save(using=self._db)        
        return user

    def create_superuser(self, email, password, **extra_fields):

        user = self.create_user(            
            email=self.normalize_email(email),
            password=password    
        )        
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user 


class Account(BaseModel, AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        help_text='유저의 이메일을 나타냅니다.',
        unique=True
    )
    username = models.CharField(
        null=True,
        blank=True,
        verbose_name='닉네임',
        help_text='유저의 닉네임을 나타냅니다.',
        max_length=32
    )
    is_superuser = models.BooleanField(
        default=False
    )
    is_staff = models.BooleanField(
        default=False
    )
    is_active = models.BooleanField(
        default=True
    )
    date_joined = models.DateField(
        auto_now_add=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AccountManager()

    class Meta:
        verbose_name = '유저'
        verbose_name_plural = '유저(들)'
        ordering = ['-date_joined']

    def __str__(self):
        return self.email
