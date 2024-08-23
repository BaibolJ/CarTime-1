from django.urls import path
from .views import CarIndexView

urlpatterns = [
    path('index/', CarIndexView.as_view())
]
