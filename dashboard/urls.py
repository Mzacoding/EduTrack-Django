from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path('student/', views.student_dashboard, name='student_dashboard'),
    path('lecturer/', views.teacher_dashboard, name='lecturer_dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path("login/", views.login_view, name="login"),
    #path("add-student/", views.add_student, name="add_student"),
    #path("add-lecturer/", views.add_lecturer, name="add_lecturer"),
]
