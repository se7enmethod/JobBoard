from django.db import models


class UserManager(models.Manager):
    def basic_validator(self, post_Data):
        errors = {}

        if len(post_Data['first_name']) < 2:
            errors['first_name'] = "First Name must be at least 2 charaters"
        if len(post_Data['last_name']) < 2:
            errors['last_name'] = "Last Name must be at least 2 charaters"
        if len(post_Data['password']) < 8:
            errors['password'] = "Password must be at least 8 charaters"
        if (post_Data['password']) != (post_Data['confirm_pw']):
            errors['confirm_pw'] = "Passwords do not match"
        return errors


class TripManager(models.Manager):
    def trip_validator(self, post_Data):
        errors = {}
        if len(post_Data['destination']) < 3:
            errors['destination'] = "A trip destination must be at least 3 charaters"
        if len(post_Data['plan']) < 2:
            errors['plan'] = "A plan must be provided"

        return errors


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Trip(models.Model):
    destination = models.CharField(max_length=45)
    start_date = models.DateField()
    end_date = models.DateField()
    plan = models.TextField(max_length=1000)
    user = models.ManyToManyField(User, related_name='trips')
    
    objects = TripManager()




