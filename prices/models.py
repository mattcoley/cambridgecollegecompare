from django.db import models


class College(models.Model):
    college_name = models.CharField(max_length=100, default='')
    rent_price = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    food_price  = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    formal_price  = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)
    formal_price_guest = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)

    def __str__(self):
        return self.college_name

