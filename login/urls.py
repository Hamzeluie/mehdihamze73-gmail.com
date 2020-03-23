from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

app_name = "user"
router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, basename='viewset')
urlpatterns = [
    path('login/', UserLogin.as_view()),
    path('apiview/', HelloApiView.as_view()),
    path('viewset/', include(router.urls)),
    path('apiview/<int:pk>', HelloApiView.as_view()),

]