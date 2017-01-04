from django.db import models

from simple_login.models import BaseUser


class User(BaseUser):
    full_name = models.CharField(max_length=255, blank=False)
    mobile_number = models.CharField(max_length=255, blank=False)
    account_activation_email_otp = None
    password_reset_email_otp = None


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False)
    location = models.CharField(max_length=255, blank=False)


class Category(models.Model):
    name = models.CharField(max_length=255, blank=False)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False)
    price = models.CharField(max_length=255, blank=False)
    image = models.ImageField(blank=True)

    class Meta:
        verbose_name = "Sub Category"
        verbose_name_plural = "Sub Categories"

    def __str__(self):
        return '{} - {}@{} SAR'.format(
            self.category.name, self.name, self.price
        )


class Service(models.Model):
    service = models.CharField(max_length=255, unique=True, blank=False)
    location = models.CharField(max_length=255, blank=False)
    max_radius = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return '{} within {} kilometers'.format(self.location, self.max_radius)


class ServiceItem(models.Model):
    item = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    request = models.ForeignKey(
        'ServiceRequest',
        related_name='service_items',
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField(blank=False)


class ServiceRequest(models.Model):
    done = models.BooleanField(default=False)
    pick_location = models.CharField(max_length=255, blank=False)
    drop_location = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return 'Request for {}'.format(self.pick_location)
