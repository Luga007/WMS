from django.db import models

class Supplier(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.first_name


class Product(models.Model):
    SIZE_CHOICES = [
        ('K', 'Kichik'),
        ('O', 'O\'rta'),
        ('KA', 'Katta'),
        ('JK', 'Juda Katta'),
    ]

    COLOUR_CHOICES = [
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Black', 'Black'),
        ('White', 'White'),
        ('Green', 'Green'),
    ]

    cloth_name = models.CharField(max_length=100)
    price = models.IntegerField()
    size = models.CharField(max_length=80, choices=SIZE_CHOICES)
    colour = models.CharField(max_length=80, choices=COLOUR_CHOICES)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cloth_name} ({self.size}, {self.colour})"




