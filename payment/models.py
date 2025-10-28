from django.db import models
from customer.models import Customer
# Create your models here.
class Payment(models.Model):
    p_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=50)
    price = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column='c_id')

    class Meta:
        managed = False
        db_table = 'payment'

    def __str__(self):
        return f"Payment #{self.p_id} by {self.customer.name if self.customer else 'Unknown'}"
