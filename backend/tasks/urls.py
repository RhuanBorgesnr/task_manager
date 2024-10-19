from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, TimeRecordViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'time-records', TimeRecordViewSet)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]