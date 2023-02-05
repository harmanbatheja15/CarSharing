from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class MyAccountManager(BaseUserManager):

    def create_user(self, email, phone, name, dob, gender, password=None):
        if not email:
            raise ValueError("Users must have an email address!")
        user = self.model(
            name = name,
            email = self.normalize_email(email),
            phone = phone,
            dob = dob,
            gender = gender,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, phone, name, dob, gender):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            name = name,
            phone = phone,
            dob = dob,
            gender = gender,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):

    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Prefer not to say', 'Prefer not to say'),
    )

    id = models.AutoField(primary_key=True)
    username = None
    email = models.EmailField(verbose_name="email", max_length=100, unique=True)
    name = models.CharField(max_length=200)
    dob = models.DateField(verbose_name="date of birth")
    gender = models.CharField(choices=gender_choices, max_length=250)
    phone = models.CharField(max_length=100, unique=True)
    
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone', 'name', 'dob', 'gender']

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

class PublishRide(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, default='')
    pickup = models.CharField(max_length=200)
    drop = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    seats = models.IntegerField()
    price = models.IntegerField()
    phone = models.CharField(max_length=100, unique=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pickup
