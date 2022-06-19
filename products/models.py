from django.db import models


# class Brend(models.Model):
#     name = models.CharField(max_length=50, unique=True)
#     slug = models.SlugField(primary_key=True, blank=True)
#
#     def __str__(self):
#         return self.name


class Product(models.Model):
    articul = models.SlugField(primary_key=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=False)
    price = models.CharField(max_length=500000, null=True, blank=False)
    discount = models.CharField(max_length=500000, null=True, blank=False)
    brend = models.CharField(max_length=100, null=True, blank=False)
    provider = models.CharField(max_length=100, null=True, blank=False)

    def __str__(self):
        return self.name, self.brend, self.provider


