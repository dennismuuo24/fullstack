from django.db import models

class Asset(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    purchase_date = models.DateField()
    asset_type = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
