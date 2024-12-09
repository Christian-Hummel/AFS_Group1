from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import random

class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, zip_code=None, city=None, password=None, role = "user"):
        user = self.model(email = email, first_name = first_name, last_name = last_name, zip_code = zip_code, city = city,role = role)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, first_name, last_name, zip_code=None, city=None, password=None, role = "admin"):
        user = self.create_user(email = email, first_name = first_name, last_name = last_name, zip_code = zip_code, city = city, role = role)
        user.is_staff = True
        user.is_superuser = True
        user.is_verified = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    role = models.CharField(max_length=20, default="user")

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    objects = CustomUserManager()

    code = models.CharField(max_length=6, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def create_code(self):
        self.code = random.randint(100000,999999)

    def __str__(self):
        return self.email


class Report(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    lon = models.FloatField()
    lat = models.FloatField()
    picture_description = models.CharField(max_length=100,default="",blank=True,null=True)
    picture = models.ImageField(upload_to='images/',default=0)
    #user_id = models.ForeignKey(CustomUser,null=False, on_delete=models.CASCADE,default=1)
    user_id = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.description} - {self.lat} - {self.lon} - {self.user_id}"

class Task(models.Model):
    description = models.CharField(max_length=100)
    managerID = models.ForeignKey(CustomUser, related_name='manager', on_delete=models.CASCADE)
    agentID = models.ForeignKey(CustomUser,related_name='agent', on_delete=models.CASCADE)
    assignedDate = models.CharField(max_length=100)
    dueDate = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.description} - {self.managerID} - {self.agentID} - {self.assignedDate} - {self.dueDate}"

class Vote(models.Model):
    report_id = models.ForeignKey(Report, on_delete=models.CASCADE)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    downvote = models.CharField(max_length=100)
    upvote = models.CharField(max_length=100)

    class Meta:
        unique_together = ('report_id','user_id')

    def __str__(self):
        return f"{self.report_id} - {self.user_id} - {self.downvote} - {self.upvote}"

class WaterLevel(models.Model):
    measuring_point = models.CharField(max_length=256)
    latitude = models.FloatField()
    longitude = models.FloatField()
    value = models.FloatField()
    unit = models.CharField(max_length=256)

    def __str__self(self):
        return self.measuring_point