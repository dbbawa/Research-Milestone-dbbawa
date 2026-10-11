from django.db import models


class Property(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural = "Properties"

    def __str__(self):
        return self.name


class Unit(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="units")
    unit_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.property.name} - {self.unit_number}"
