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


class JobManager(models.Manager):
    def job_validator(self, post_Data):
        errors = {}
        if len(post_Data['job_title']) < 3:
            errors['job_title'] = "Job title must consist of at least 3 charaters"
        if len(post_Data['location']) < 1:
            errors['location'] = "A location must be provided"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Job(models.Model):
    job_title=models.CharField(max_length=45)
    location = models.CharField(max_length=45)
    description = models.TextField(max_length=1000)
    category = models.TextField(max_length=45)
    user = models.ManyToManyField(User, related_name='jobs')
    objects = JobManager()
