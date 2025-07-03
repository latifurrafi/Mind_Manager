from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, index, PredictPriorityView, GeminiChatBotView, register
from django.contrib.auth import views as auth_views

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', register, name='register'),  # fixed line
    path('api/', include(router.urls)),
    path('api/predict-priority/', PredictPriorityView.as_view(), name='predict-priority'),
    path('api/chatbot/', GeminiChatBotView.as_view(), name='chatbot'),
]
