from django.db import models

# Create your models here.
class Report(models.Model):
    r_id = models.AutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    report = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report'
