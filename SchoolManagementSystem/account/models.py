from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=20)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    batch = models.CharField(max_length=20)
    
    def update_profile(self, **kwargs):
        for field, value in kwargs.items():
            setattr(self, field, value)
        self.save()
    
    def __str__(self):
        return self.user.username + ' (Student)'

class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher_id = models.CharField(max_length=20)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    
    def update_profile(self, **kwargs):
        for field, value in kwargs.items():
            setattr(self, field, value)
        self.save()
    
    def __str__(self):
        return self.user.username + ' (Teacher)'
