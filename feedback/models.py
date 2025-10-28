from django.db import models
from customer.models import Customer
# Create your models here.
class Feedback(models.Model):
    f_id = models.AutoField(primary_key=True)
    feedback = models.CharField(max_length=150)
    date = models.DateField()
    time = models.TimeField()
    # c_id = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column='c_id')

    class Meta:
        managed = False
        db_table = 'feedback'
