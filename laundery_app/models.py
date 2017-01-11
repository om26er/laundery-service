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
    drop_on_pickup_location = models.BooleanField(default=True)
    pickup_house_number = models.CharField(max_length=255, blank=False)
    pickup_city = models.CharField(max_length=255, blank=False)
    pickup_street = models.CharField(max_length=255, blank=False)
    pickup_zip = models.CharField(max_length=255, blank=False)
    drop_house_number = models.CharField(max_length=255, blank=True)
    drop_city = models.CharField(max_length=255, blank=True)
    drop_street = models.CharField(max_length=255, blank=True)
    drop_zip = models.CharField(max_length=255, blank=True)


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

    @property
    def name(self):
        return self.item.name


class ServiceRequest(models.Model):
    user = models.ForeignKey(User, null=True)
    done = models.BooleanField(default=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return 'Request for {}'.format(self.address.location)
