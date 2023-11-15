from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    
    def __str__(self):
        return self.title
    
    title = models.CharField(max_length=50)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=60)
    description = models.TextField()
    image = models.CharField(max_length=300)
    # sell_by = models.ForeignKey(User,on_delete=models.CASCADE)


class Order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=40)
    address = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    zip = models.CharField(max_length=6) 
    total = models.CharField(max_length=200)
    
    
class Cart(models.Model):
    product = models.CharField(max_length=1000)
    quantity = models.CharField(max_length=25)
    
    
class CartMapping(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Product, on_delete=models.CASCADE)