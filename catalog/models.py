from django.db import models
from django.contrib.auth.models import User
from django.db.models import Model
from django.shortcuts import reverse


CATEGORY_CHOICES = (
    ('S', 'Man Shirt'),
    ('SW', 'Sport Wear'),
    ('OW', 'Outwear')
)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)

NEWO_OLD_CHOICES = (
    ('N', 'new'),
    ('O', 'old'),
)


class Item(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    discount_price = models.IntegerField()
    slug = models.SlugField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={"slug": self.slug})

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.BooleanField(default=False)
    start_order = models.DateTimeField(auto_now_add=True)
    ordered = models.DateTimeField()

    def __str__(self):
        return self.user.username


class SliderItem(models.Model):
    titile = models.CharField(max_length=200)
    descTitle = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    pageLink = models.URLField()

    def __str__(self):
        return self.titile
