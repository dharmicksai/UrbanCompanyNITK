from django.urls import path, include
from django.contrib.auth.decorators import login_required
from . import views
from .views import *

urlpatterns = [

    path('', customer.as_view(), name = "ucnitk"),
    path('add-something', views.add_something, name = "add-something"),
    # path('order-service', views.order_service, name = "order-service"),
    path('service-provider', login_required(service_provider.as_view(), login_url='/authentication/login'), name = "service-provider"),
    path('order/<int:pk>/', views.order_detail, name='order-detail'),
    path('order/new/', login_required(OrderCreateView.as_view(), login_url='/authentication/login'), name='order-create'),
    path('review/<int:pk>/',views.review, name='review'),
    path('your-orders', login_required(your_orders.as_view(), login_url='/authentication/login'), name = "your-orders"),
    path('issues/', login_required(your_issues.as_view(), login_url='/authentication/login'), name = "issues"),
    path('issues/new/', login_required(create_issue.as_view(), login_url='/authentication/login'), name = "create_issue"),
    path('view_review', login_required(view_review.as_view(), login_url='/authentication/login'), name = "view_review"),
    path('accepted-orders', login_required(accepted_orders.as_view(), login_url='/authentication/login'), name = "accepted-orders"),
    path('accept_order/<int:pk>/', views.accept_order, name='accept-order'),
    path('cancel_order/<int:pk>/', views.cancel_order, name='cancel-order'),
    path('finish_order/<int:pk>/', views.finish_order, name='finish-order'),
    path('delete_order/<int:pk>/', views.delete_order, name='delete-order'),
    path('confirm_cash_payment/<int:pk>/', views.confirm_cash_payment, name='confirm-cash-payment'),

    #payment callback handler
    path('handlerequest/', views.handlerequest, name = 'handlerequest'),
]
