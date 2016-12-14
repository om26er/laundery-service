from django.db import models

from simple_login.models import BaseUser


class User(BaseUser):
    full_name = models.CharField(max_length=255, blank=False)
    mobile_number = models.CharField(max_length=255, blank=False)
    account_activation_sms_otp = None
    password_reset_sms_otp = None


class Address(models.Model):
    user = models.ForeignKey(User)
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
    category = models.ForeignKey(Category)
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
