from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app_main.views import *

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Suv yetkazib berish tizimi',
        default_version='v1.0',
        description='Front-end, Android, Desktop dasturchilar uchun suv yetkazib berish tizimi API DOCS',
        contact=openapi.Contact(email='cbekoder@gmail.com'),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register('suv', SuvModelViewSet)
router.register('mijozlar', MijozModelViewSet)
router.register('buyurtmalar', BuyurtmaModelViewSet)
router.register('adminlar', AdminModelViewSet)
router.register('haydovchilar', HaydovchiModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
]
