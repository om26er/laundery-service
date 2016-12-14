from django.contrib import admin
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Group

from laundery_app.models import User, Category, SubCategory


class UserAdmin(admin.ModelAdmin):
    class Meta:
        model = User


class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category


class SubCategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = SubCategory


admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.unregister(Token)
admin.site.unregister(Group)
