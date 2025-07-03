from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, index, PredictPriorityView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', index, name='index'),
    path('api/', include(router.urls)),
    path('api/predict-priority/', PredictPriorityView.as_view(), name='predict-priority'),
] + router.urls
