from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name = "ucnitk"),
    path('add-something', views.add_something, name = "add-something"),
    path('order-service', views.order_service, name = "order-service"),
]
