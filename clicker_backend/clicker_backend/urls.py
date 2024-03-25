from django.contrib import admin
from django.urls import path, include
from clicker_app import views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework.permissions import AllowAny

router = routers.DefaultRouter()
router.register(r'user', views.ClickerViewSet, 'user')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
    path('login/', TokenObtainPairView(permissions_classes=[AllowAny]).as_view(), name='login'),
    path('token/refresh/', TokenRefreshView(permissions_classes=[AllowAny]).as_view(), name='token_refresh'),
]
