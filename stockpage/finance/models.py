from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

# Create your models here.
class Stock(models.Model):
    ticker = models.CharField(max_length=4,primary_key=True)
    company = models.CharField(max_length=20)

    def __str__(self):
        return self.ticker

class Detail(models.Model):
    sharperatio = models.FloatField(null=True, blank=True, default=None)
    volatility = models.FloatField(null=True, blank=True, default=None)
    expected_return = models.FloatField(null=True, blank=True, default=None)
    momentum = models.FloatField(null=True, blank=True, default=None)
    created_date = models.DateTimeField(default=timezone.now)
    analyzed_stock = models.ForeignKey(Stock,on_delete=models.CASCADE)

    def __str__(self):
        return "Analysis of {} which was created {}".format(self.analyzed_stock,self.created_date)

class DisplaySr(models.Model):
    sharperatio = models.FloatField(null=True, blank=True, default=None)
    created_date = models.DateTimeField(default=timezone.now)
    analyzed_stock = models.ForeignKey(Stock,on_delete=models.CASCADE)

    def __str__(self):
        return "{} with SR of: {}".format(self.analyzed_stock,self.sharperatio)
