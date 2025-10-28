from django.db import models

# Create your models here.

class Warden(models.Model):
    w_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    email = models.CharField(max_length=50)
    phone = models.IntegerField()
    status = models.CharField(max_length=50)
    gender = models.CharField(max_length=30)
    age = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'warden'