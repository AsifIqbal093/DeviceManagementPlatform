# yourapp/models.py
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email!')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.is_superuser = False
        user.is_staff = False
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create, save and return a super user."""
        if not email:
            raise ValueError('User must have an email!')
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.role = 'Lev Manager'
        user.save(using=self._db)

        return user


class Accounts(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    LEV_OPERATOR = 'lev_operator'
    LEV_ENGINEER = 'lev_engineer'
    LEV_MANAGER = 'lev_manager'
    OWNER = 'owner'

    ROLE_CHOICES = [
        (LEV_OPERATOR, 'Lev Operator'),
        (LEV_ENGINEER, 'Lev Engineer'),
        (LEV_MANAGER, 'Lev Manager'),
        (OWNER, 'Owner'),
    ]

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=OWNER)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        """
        Returns a string representation of the user name.

        Returns:
        - str: The user name.
        """
        return self.name
