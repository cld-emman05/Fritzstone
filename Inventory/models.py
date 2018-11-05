from django.db import models
from datetime import datetime

# Create your models here.

class Inventory(models.Model):
    product = models.CharField(max_length=50)
    category = models.CharField(max_length=15)
    price = models.DecimalField(max_digits = 12, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(default = datetime.now, blank=True)
    def __str__(self):
        return self.product
    class Meta:
        verbose_name_plural = 'Inventories'
