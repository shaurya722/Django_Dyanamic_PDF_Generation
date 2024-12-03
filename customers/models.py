from django.db import models

# Create your models here.

class Customer(models.Model):

    name = models.CharField( max_length=50)
    logo = models.ImageField()
    description = models.TextField()
    upadated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name