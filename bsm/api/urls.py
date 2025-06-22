
from django.urls import path
from .views import SampleItemView, BlackscholesView


urlpatterns = [
    path('items/', SampleItemView.as_view(), name='items'),
    path('calculate/', BlackscholesView.as_view(), name='calculate'),
]
