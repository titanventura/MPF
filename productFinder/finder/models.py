from django.db import models

# Create your models here.

class brand(models.Model):
    name            = models.CharField(max_length=30,unique=True)
    position        = models.IntegerField(null=True,default=0)
    years           = models.IntegerField()
    description     = models.TextField(max_length=1000)
    logo            = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name + " : position : " + str(self.position)

class product(models.Model):
    prodbrand       = models.ForeignKey(brand,on_delete=models.CASCADE)
    model           = models.CharField(max_length=50,unique='True')
    specification   = models.TextField(max_length=10000)
    rating          = models.IntegerField(default=0)
    year_of_launch  = models.IntegerField()
    photo           = models.CharField(max_length=1000,null=True)
