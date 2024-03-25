from django.contrib import admin
from django.urls import path, include
from clicker_app import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', views.ClickerViewSet, 'user')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls))
]
