
from django.db import models
#추가
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    pass1 = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    gender = models.IntegerField(default=0)
    tel = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    picture = models.CharField(max_length=200)
    
    def __str__(self):
        return self.id + ":" + self.name + ":" + self.pass1   
    
    
#추가
