from django.urls import path
from . import views
from .views import *

urlpatterns = [

    path('', customer.as_view(), name = "ucnitk"),
    path('add-something', views.add_something, name = "add-something"),
    path('order-service', views.order_service, name = "order-service"),
    path('service-provider', service_provider.as_view(), name = "service-provider")
]
