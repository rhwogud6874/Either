from django.urls import path, include
from . import views

app_name = "questions"

urlpatterns = [
    path('', views.index, name="index"),

    path('create/', views.create, name="create"),
    path('<int:id>/detail/', views.detail, name="detail"),
    path('random_question/', views.random_question, name="random_question"),

    path('<int:id>/update/', views.update, name="update"),
    path('<int:id>/delete/', views.delete, name="delete"),

    path('<int:question_id>/choice/', views.choice_create, name="choice_create"),
    path('<int:question_id>/choice/<int:pick>/', views.choice_nocomment, name="choice_nocomment"),

    path('<int:question_id>/choice/<int:choice_id>/delete/', views.choice_delete, name="choice_delete"),
    
]