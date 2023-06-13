from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class AdministratorManager(BaseUserManager):
    def create_user(self, email, username, name, last_name, password = None):
        if not email:
            raise ValueError('El usuario debe tener un correo electronico')
        
        user = self.model(
            username = username,
            name = name,
            last_name = last_name,
            email = self.normalize_email(email)
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, name, last_name, password = None):
        user = self.create_user(
            email = email,
            username = username,
            name = name,
            last_name = last_name,
            password = password
        )
        user.user_administrator = True
        user.save()
        return user

class Administrator(AbstractBaseUser):
    username = models.CharField('username', unique = True, max_length = 100)
    email = models.EmailField('email', unique = True, max_length = 150)
    name = models.CharField('name', max_length = 100, blank = True)
    last_name = models.CharField('last_name', max_length = 100, blank = True)
    user_active = models.BooleanField(default = True)
    user_administrator = models.BooleanField(default = False)
    objects = AdministratorManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'last_name']

    def __str__(self):
        return f'{self.username}, {self.name}, {self.last_name}'

    def has_perm(self, perm, obj = None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.user_administrator

    class Meta:
        db_table = 'administradores'