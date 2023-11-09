from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class category(models.Model):
    cate_name = models.CharField(max_length=300)
    imge_url = models.CharField(max_length=2000,blank=True,default=False)
    
    def __str__(self):
        return self.cate_name





class Products(models.Model):
    title = models.CharField(max_length=300)
    categories = models.ForeignKey(category , on_delete=models.CASCADE, default=True, null=False)
    price = models.IntegerField()
    img_url = models.CharField(max_length=2000,blank=True,default=False)
    p_avl = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.title




class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    items= models.ManyToManyField(Products)
    


