from django.db import models

# Create your models here.

class Superindentent(models.Model):
    s_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=150)
    phone = models.IntegerField()
    email = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'superindentent'


