from django.urls import path
from . import views

 
 

urlpatterns = [
    path('add/', views.add_student_view, name='add'),
    path('list/', views.students_list_view, name='list'),
    path('update/<str:pk>/', views.update_student_view, name='update'),
    path('delete/<str:pk>/', views.delete_student_view, name='delete'),



    path('lecture_view/add/', views.add_lecture_view, name='lecture_view/add'),
    path('lecture_view/list/', views.lecture_list_view, name='lecture_view/list'),
    path('lecture_view/update/<str:pk>/', views.update_lecture_view, name='lecture_view/update'),
    path('lecture_view/delete/<str:pk>/', views.delete_lecture_view, name='lecture_view/delete'),
]