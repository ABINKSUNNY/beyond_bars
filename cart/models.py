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


class CartItem(models.Model):
    customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE, null=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.food.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.food.name}"

class Purchase(models.Model):
    pu_id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey('customer.Customer', on_delete=models.SET_NULL, null=True)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    payment_id = models.CharField(max_length=100)
    order_id = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Purchase of {self.quantity} x {self.food.name} by {self.customer}"


