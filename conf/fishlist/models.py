from django.db import models


class Nomal(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=15)
    shape = models.CharField(max_length=5000)
    ecology = models.CharField(max_length=5000)
    place = models.CharField(max_length=5000)
    eat = models.CharField(max_length=500)




class Poison(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=15)
    shape = models.CharField(max_length=5000)
    ecology = models.CharField(max_length=5000)
    place = models.CharField(max_length=5000)
    eat = models.CharField(max_length=500)





class Extinct(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=15)
    reason = models.CharField(max_length=5000)
    shape = models.CharField(max_length=5000)
    ecology = models.CharField(max_length=5000)
    place = models.CharField(max_length=5000)


        
    def __str__(self):
        return self.id + ':' + self.name + ':' +self.reason
        





