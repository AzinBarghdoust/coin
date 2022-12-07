from django.contrib.auth.base_user import BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, username, password, **extra_fields):
        """
        Creates and saves a User with the given username and password.
        """

        user = self.model(email=email, username=username, password=password, **extra_fields)
        user.set_password(password)

        user.save()
        return user

    def create_superuser(self, email, username, password, **extra_fields):
        """
        Creates and saves a superuser with the given username and password.
        """

        user = self.create_user(
            email,
            username,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
