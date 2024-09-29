from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
router =DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
]
