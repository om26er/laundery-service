from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from laundery_app.models import User, Address, Category


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True)
    full_name = serializers.CharField(required=True)
    mobile_number = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'password',
            'full_name',
            'mobile_number',
        )


class AddressSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    location = serializers.CharField(required=True)

    class Meta:
        model = Address
        fields = (
            'name',
            'location',
        )


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)

    class Meta:
        model = Category
        fields = ('id', 'name', )


class SubCategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    price = serializers.CharField(required=True)
    image = serializers.ImageField(required=False)

    class Meta:
        model = Category
        fields = ('name', 'price', 'image', )
