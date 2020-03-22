from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
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