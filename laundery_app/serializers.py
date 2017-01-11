from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from laundery_app.models import (
    User,
    Address,
    Category,
    SubCategory,
    ServiceRequest,
    ServiceItem,
)


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
    class Meta:
        model = Address
        fields = (
            'id',
            'name',
            'location',
            'drop_on_pickup_location',
            'pickup_house_number',
            'pickup_city',
            'pickup_street',
            'pickup_zip',
            'drop_house_number',
            'drop_city',
            'drop_street',
            'drop_zip',
        )


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
        )


class SubCategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    price = serializers.CharField(required=True)
    image = serializers.ImageField(required=False)

    class Meta:
        model = SubCategory
        fields = (
            'id',
            'name',
            'price',
            'image',
        )


class ServiceItemSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(required=True)
    name = serializers.CharField(read_only=True)

    class Meta:
        model = ServiceItem
        fields = (
            'item',
            'quantity',
            'name',
        )


class ServiceRequestValidationSerializer(serializers.Serializer):
    service_items = serializers.ListField(required=True)
    address = serializers.IntegerField(required=True)
    user = serializers.IntegerField(required=True)


class ServiceRequestSerializer(serializers.ModelSerializer):
    service_items = ServiceItemSerializer(many=True)
    address = AddressSerializer(read_only=True)
    done = serializers.BooleanField(read_only=True)
    created = serializers.DateTimeField(read_only=True)

    class Meta:
        model = ServiceRequest
        fields = (
            'done',
            'address',
            'service_items',
            'user',
            'created'
        )

    def run_validation(self, data=None):
        self._address_id = data.get('address')
        return super().run_validation(data)

    def create(self, validated_data):
        items_data = validated_data.pop('service_items')
        request = ServiceRequest.objects.create(
            address_id=self._address_id, user=validated_data.get('user'))
        for item_data in items_data:
            _item = item_data.pop('item')
            ServiceItem.objects.create(
                item=_item, request=request, **item_data)
        return request
