from django.urls import path
from . import views
from .views import *

urlpatterns = [

    path('', customer.as_view(), name = "ucnitk"),
    path('add-something', views.add_something, name = "add-something"),
    path('order-service', views.order_service, name = "order-service"),
    path('service-provider', service_provider.as_view(), name = "service-provider"),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('your-orders', your_orders.as_view(), name = "your-orders"),
    path('accepted-orders', accepted_orders.as_view(), name = "accepted-orders"),
]
