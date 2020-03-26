"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register('viewset_sectiongroup', ViewSetSectionGroup, basename='SectionGroup')
router.register('model_viewset_sectiongroup', ModelViewSetSectionGroup, basename='ModelSectionGroup')

router.register('viewset_section', ViewSetSection, basename='Section')
router.register('model_viewset_section', ModelViewSetSection, basename='ModelSection')

app_name = 'section'
urlpatterns = [
    path('viewset/', include(router.urls), name='viewset'),

    path('apiview/', ApiViewSectionGroup.as_view()),
    path('apiview/<int:pk>/', ApiViewSectionGroup.as_view()),

    path('apiview/section/', ApiViewSectionGroup.as_view()),
    path('apiview/section/<int:pk>/', ApiViewSectionGroup.as_view()),

    path('', SectionGroupIndexView.as_view(), name='home'),
    path('create/', SectionGroupCreateView.as_view(), name='group_create'),
    path('<int:group_id>/delete/', SectionGroupDeleteView.as_view(), name='group_delete'),
    path('<int:group_id>/update/', SectionGroupUpdateView.as_view(), name='group_update'),

    path('<int:group_id>/', SectionIndexView.as_view(), name='home'),
    path('<int:group_id>/create/', SectionCreateView.as_view()),
    path('<int:group_id>/<int:section_id>/delete/', SectionDeleteView.as_view()),
    path('<int:group_id>/<int:section_id>/update/', SectionUpdateView.as_view()),
]