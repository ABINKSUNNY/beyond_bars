from django.db import models

# Create your models here.
class Stock(models.Model):
    st_id = models.AutoField(primary_key=True)
    stock = models.IntegerField()
    status = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    quandity = models.IntegerField()
    price = models.IntegerField()
    food = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'stock'
