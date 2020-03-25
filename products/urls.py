from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
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
router = DefaultRouter()
router.register('viewset_product', views.ViewSetProduct, basename='product_viewset')
router.register('viewset_productgroup', views.ViewSetProductGroup, basename='productgroup_viewset')

router.register('model_viewset_product', views.ModelViewSetProduct, basename='product_viewset')
router.register('model_viewset_productgroup', views.ModelViewSetProductGroup, basename='productgroup_viewset')


app_name = 'products'
urlpatterns = [
    path('viewset/', include(router.urls), name='viewset'),

    path('apiview/', views.ApiProductGroupView.as_view(), name='api_group'),
    path('apiview/<int:pk>/', views.ApiProductGroupView.as_view(), name='api_group'),

    path('apiview/product/', views.ApiProductView.as_view(), name='api_product'),
    path('apiview/product/<int:pk>', views.ApiProductView.as_view(), name='api_product'),


    path('', views.ProductGroupIndexView.as_view(), name='home'),
    path('create/', views.ProductGroupCreateView.as_view(), name='group_create'),
    path('<int:group_id>/delete/', views.ProductGroupDeleteView.as_view()),
    path('<int:group_id>/update/', views.ProductGroupUpdateView.as_view()),


    path('<int:group_id>/', views.ProductIndexView.as_view(), name='products'),
    path('<int:group_id>/create/', views.ProductCreateView.as_view()),
    path('<int:group_id>/<int:product_id>/delete/', views.ProductDeleteView.as_view(), name='products_delete'),
    path('<int:group_id>/<int:product_id>/update/', views.ProductUpdateView.as_view(), name='products_update'),

]
