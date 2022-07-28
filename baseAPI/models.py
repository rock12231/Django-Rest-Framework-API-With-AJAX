from django.db import models


# id,name,position,salary,start_date,office,extn
class Emp(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    position = models.CharField(max_length=100, blank=True, default='')
    salary = models.CharField(max_length=100, blank=True, default='')
    start_date = models.DateField()
    office = models.CharField(max_length=100, blank=True, default='')
    extn = models.IntegerField(blank=True, default='0')
    
    class Meta:
        ordering = ['start_date']
        