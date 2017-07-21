from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Restaurant(models.Model):
    added_by = models.OneToOneField(User)
    name = models.CharField(max_length=120)
    street = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)
    # img

    def __str__(self):
            return self.name


class Order(models.Model):
    user = models.ForeignKey(User)
    restaurant = models.ForeignKey(Restaurant)
    date = models.DateTimeField()
    item = models.CharField(max_length=120)
    customization = models.CharField(max_length=120, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=6, blank=True, null=True)

    def __str__(self):
            return f"{self.date} | {self.restaurant} | {self.item}"
