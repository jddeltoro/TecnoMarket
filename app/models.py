from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class  Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    is_new = models.BooleanField()
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    creation_date = models.DateField()

    def __str__(self) -> str:
        return self.name