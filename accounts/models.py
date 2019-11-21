from django.db import models

# Create your models here.
class reg(models.Model):

    username = models.CharField(max_length=100,default='noname')
    email= models.EmailField(default='noemail@gmail.com')
    phone = models.CharField(max_length=12,default='00000000000')
    password = models.CharField(max_length=25,default='1234')
