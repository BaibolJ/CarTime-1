from rest_framework import serializers

from .models import *


class CarIndexSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = (
            'id',
            'title',
            'price_day',
            'img_main',
            'volume',
            'power',
            'fuel_type',
            'gearbox',
            'type_car_body',
            'status',
            'year'
        )


class CarCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title'
        )

