from django.db import models

class Location(models.Model):
    street_name = models.CharField(max_length=100)
    district = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.street_name}, {self.district}"


    def __str__(self):
        return self.street_name

