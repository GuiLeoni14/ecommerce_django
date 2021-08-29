from django.db import models

class ProductManager(models.Manager):
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id = id)
        if qs.count() == 1:
            return qs.first()
        return None


class Product(models.Model): #product_category
    title       = models.CharField(max_length=120)
    description = models.TextField()
    price       = models.DecimalField(decimal_places=2, max_digits=20, default=100.00)

    objects = ProductManager()

    def __str__(self):
        return self.title
        