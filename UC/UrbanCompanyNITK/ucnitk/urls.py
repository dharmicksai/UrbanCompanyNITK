from django.urls import path
from . import views
from .views import *

urlpatterns = [

    path('', customer.as_view(), name = "ucnitk"),
    path('add-something', views.add_something, name = "add-something"),
    # path('order-service', views.order_service, name = "order-service"),
    path('service-provider', service_provider.as_view(), name = "service-provider"),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('order/new/', OrderCreateView.as_view(), name='order-create'),
    path('review/<int:pk>/',views.review, name='review'),
    path('your-orders', your_orders.as_view(), name = "your-orders"),
    path('issues/', your_issues.as_view(), name = "issues"),
    path('issues/new/', create_issue.as_view(), name = "create_issue"),
    path('view_review', view_review.as_view(), name = "view_review"),
    path('accepted-orders', accepted_orders.as_view(), name = "accepted-orders"),
    path('accept_order/<int:pk>/', views.accept_order, name='accept-order'),
    path('cancel_order/<int:pk>/', views.cancel_order, name='cancel-order'),
    path('finish_order/<int:pk>/', views.finish_order, name='finish-order'),
    path('delete_order/<int:pk>/', views.delete_order, name='delete-order'),
]
