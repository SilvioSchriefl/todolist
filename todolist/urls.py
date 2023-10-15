from django.urls import include, path
from rest_framework import routers

from todo.views import TodoViewSet


router = routers.DefaultRouter()
router.register(r'todos', TodoViewSet)

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
