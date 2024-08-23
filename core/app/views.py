from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from .serializers import *
from .models import Car, Category


class CarIndexView(APIView):
    @swagger_auto_schema(
        operation_description="Получить категории и топ 10 машин",
        responses={200: openapi.Response('OK', CarIndexSerializers(many=True))},
        # manual_parameters=[
        #     openapi.Parameter('some_param', openapi.IN_QUERY, description="Пример параметра", type=openapi.TYPE_STRING)
        # ]
    )
    def get(self, request):
        # Получение всех категорий
        categories = Category.objects.all()
        # Получение топ 10 машин
        cars = Car.objects.all()[:10]

        category_serializers = CarCategorySerializers(categories, many=True)
        car_serializers = CarIndexSerializers(cars, many=True)

        data = {
            "categories": category_serializers.data,
            "cars": car_serializers.data,
        }

        return Response(data)

