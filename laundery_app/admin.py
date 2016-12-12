from django.contrib import admin
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Group

from laundery_app.models import User, Category


class UserAdmin(admin.ModelAdmin):
    class Meta:
        model = User


class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category


admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.unregister(Token)
admin.site.unregister(Group)
