from django.db import models

class Customer(models.Model):
    c_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    adress = models.CharField(max_length=150)
    gender = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    status = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'customer'

