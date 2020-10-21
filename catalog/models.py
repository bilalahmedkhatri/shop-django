from django.db import models
from django.contrib.auth.models import User
# Create your models here.


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
    label = models.CharField(choices=LABEL_CHOICES, max_length=2)
    description = models.TextField()

    def __str__(self):
        return self.title


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
