from django.db import models

class Product(models.Model):
    
    def __str__(self):
        return self.title
    
    title = models.CharField(max_length=50)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=60)
    description = models.TextField()
    image = models.CharField(max_length=300)

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