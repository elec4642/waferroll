from django.db import models

# Create your models here.
class milk(models.Model):
    产品=models.CharField(max_length = 20)
    供货价_含运费= models.FloatField()
    零售价_含运费= models.FloatField()
    id = models.IntegerField(primary_key = True)