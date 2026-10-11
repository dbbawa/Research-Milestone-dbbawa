from django.db import models


class Property(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to='property_images/', blank=True, null=True)
    bedrooms = models.PositiveIntegerField(default=0)
    bathrooms = models.PositiveIntegerField(default=0)
    monthly_rent = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    class Meta:
        verbose_name_plural = "Properties"

    def __str__(self):
        return self.name


class Unit(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="units")
    unit_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.property.name} - {self.unit_number}"
