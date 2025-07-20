from django.db import models

class Category(models.Model) :
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Types(models.Model) :
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null = True, related_name='categories')
    
    def __str__(self):
        return self.name
    
    
class Shop(models.Model) :
    
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='shop')
    content = models.TextField()
    type = models.ForeignKey(Types, on_delete=models.SET_NULL, null = True, related_name='shops')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.title


class Order(models.Model) :
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    card_number = models.CharField(max_length=16)
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return self.first_name
    