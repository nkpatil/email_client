from django.urls import path, include
from rest_framework.routers import DefaultRouter

from mail import views, viewsets

router_v1 = DefaultRouter()
router_v1.register('mail', viewsets.MailViewset)

urlpatterns = [
    path('', views.MailView.as_view(), name='mail'),
    path('v1/', include(router_v1.urls)),
]
