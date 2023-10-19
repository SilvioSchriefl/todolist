from django.urls import path
from todo.views import  LoginView, TodoItemView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('todos/', TodoItemView.as_view()),
    path('todos/<int:pk>/', TodoItemView.as_view())
]
