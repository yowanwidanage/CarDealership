from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()
    is_available = models.BooleanField(default=True)
    fuel_type = models.CharField(max_length=50, default='Petrol')

    def __str__(self):
        return self.name
