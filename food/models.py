

# Create your models here.
from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='foods/', blank=True, null=True)
    quantity = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)

    # stock = models.PositiveIntegerField(default=0)  # new field

    def __str__(self):
        return self.name