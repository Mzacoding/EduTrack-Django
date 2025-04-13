from django.urls import path
from . import views

 
 

urlpatterns = [
    path('add/', views.add_student_view, name='add'),
    path('list/', views.students_list_view, name='list'),
    path('update/<str:pk>/', views.update_student_view, name='update'),
    path('delete/<str:pk>/', views.delete_student_view, name='delete'),
]