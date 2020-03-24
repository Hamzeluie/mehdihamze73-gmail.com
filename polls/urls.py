from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('question_model_viewset', views.QuestionModelViewSet, basename='QModel_Viewset')
router.register('choice_model_viewset', views.ChoiceModelViewSet, basename='CModel_Viewset')

router.register('question_viewset', views.QuestionViewSet, basename='QViewset')
router.register('choice_viewset', views.ChoiceViewSet, basename='CViewset')

app_name = 'polls'
urlpatterns = [
    path('viewset/', include(router.urls)),
    path('apiview/', views.QuestionApiview.as_view()),
    path('apiview/<int:pk>/', views.QuestionApiview.as_view()),

    path('apiview/choice/', views.ChoiceApiview.as_view()),
    path('apiview/choice/<int:pk>/', views.ChoiceApiview.as_view()),
    # path('apiview/<int:pk>/choice/<int:c_id>/', views.ChoiceApiview.as_view()),




    path('', views.QuestionIndexView.as_view(), name='index'),
    path('<int:pk>/result/', views.QuestionResultView.as_view(), name='result'),
    path('<int:question_id>/vote/', views.questionvote, name='vote'),
    path('create/', views.QuestionCreateView.as_view(), name='create'),
    path('<int:question_id>/delete/', views.QuestionDeleteView.as_view(), name='delete'),
    path('<int:question_id>/update/', views.QuestionUpdateView.as_view(), name='update'),

    path('<int:question_id>/choice/', views.ChoiceIndexView.as_view(), name='index'),
    path('<int:question_id>/choice/create/', views.ChoiceCreateView.as_view(), name='create'),
    path('<int:question_id>/choice/<int:choice_id>/update/', views.ChoiceUpdateView.as_view(), name='update'),
    path('<int:pk>/choice/<int:choice_id>/delete/', views.ChoiceDeleteView.as_view(), name='delete'),
    ]