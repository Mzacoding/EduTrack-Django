import csv
from django.shortcuts import render, HttpResponse
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from .forms import *
from .models import *

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

from django.shortcuts import render
from django.utils.safestring import mark_safe
 
import datetime
 
 
 
 


 

def home_view(request):
    return render(request, "Home/home.html")

def get_current_class():
    """Mock function to retrieve the current class based on time."""
    timetable = {
        "08:00-09:30": "Math",
        "10:00-11:30": "Science",
        "13:00-21:30": "History",
    }

    now = datetime.datetime.now().strftime("%H:%M")

    for time_range, subject in timetable.items():
        start, end = time_range.split("-")
        if start <= now <= end:
            return subject

    return None   

import json
from django.utils.safestring import mark_safe
from django.shortcuts import render

def student_dashboard(request):
    subjects_registered = [
        {"name": "Math", "code": "MATH101", "course": "BSc Engineering", "final_marks": 65, "required_marks": 50, "image": "images/math.jpg"},
        {"name": "Science", "code": "SCI101", "course": "BSc Physics", "final_marks": 80, "required_marks": 50, "image": "images/science.jpg"},
        {"name": "History", "code": "HIST101", "course": "BA History", "final_marks": 45, "required_marks": 50, "image": "images/history.jpg"},
    ]

    performance_data = [{"subject": sub["name"], "marks": sub["final_marks"]} for sub in subjects_registered]

    current_class = get_current_class()

    context = {
        "user": {
            "name": "Nyiko Mkansi",
            "student_number": "221155230",
            "profile_pic": "dashboard/styles/nyiko.jpg",
            "Role": "Student",
        },
        "subjects_registered": subjects_registered,
        "performance_data": mark_safe(json.dumps(performance_data)),  # Safe JSON data for charts
        "current_class": current_class,  # Controls attendance section
        "study_tips": [
            "Attend all lectures and take good notes.",
            "Use past exam papers to practice questions.",
            "Join study groups for better understanding.",
            "Increase participation in class discussions.",
        ],
    }
    return render(request, "dashboard/student_dashboard.html", context)







def admin_dashboard(request):
    context = {
        "admin": {
            "name": "Nyiko Mkansi",
            "Role":'Admin User',
           "profile_pic": "dashboard/styles/nyiko.jpg",
        },
        "user_management": [
            {"name": "John Doe", "role": "Student"},
            {"name": "Jane Roe", "role": "Student"},
            {"name": "Ms. Smith", "role": "Teacher"},
        ],
        "system_logs": [
            {"date": "2025-05-01", "action": "User John Doe updated profile"},
            {"date": "2025-05-02", "action": "Admin added new user: Jane Roe"},
            {"date": "2025-05-03", "action": "Password reset requested for Ms. Smith"},
        ],
        "roles_permissions": [
            {"user": "John Doe", "role": "Student", "permissions": ["View Grades", "Submit Assignments"]},
            {"user": "Jane Roe", "role": "Student", "permissions": ["View Grades", "Submit Assignments"]},
            {"user": "Ms. Smith", "role": "Teacher", "permissions": ["Manage Classes", "Grade Students"]},
        ],
        "system_settings": {
            "backup_schedule": "Daily at 2 AM",
            "security_level": "High",
            "maintenance_mode": False,
        },
        "issue_tracking": [
            {"ticket_id": "001", "user": "John Doe", "issue": "Login failure", "status": "Resolved"},
            {"ticket_id": "002", "user": "Jane Roe", "issue": "Grade missing", "status": "Pending"},
            {"ticket_id": "003", "user": "Ms. Smith", "issue": "Access to reports denied", "status": "Investigating"},
        ],
        "announcements": [
            {"title": "Scheduled Maintenance", "message": "System will be down for maintenance on May 10."},
            {"title": "Policy Update", "message": "New grading policies have been implemented."},
        ]
    }
    return render(request, "dashboard/admin_dashboard.html", context)



 
def teacher_dashboard(request):
     
    grade_list = [
        {"student": "Nyiko Mkansi", "grade": "A"},
        {"student": "Walker Mkansi", "grade": "B"},
        {"student": "Messie Mathipa", "grade": "A-"},
        {"student": "Nyiko Mkansi", "grade": "A"},
        {"student": "Walker Mkansi", "grade": "B"},
        {"student": "Messie Mathipa", "grade": "A-"},
 
    ]
    
 
    attendance_list = [
        {"student": "Nyiko Mkansi", "status": "Present"},
        {"student": "Walker Mkansi", "status": "Absent"},
        {"student": "Messie Mathipa", "status": "Present"},
        {"student": "Londa Ray", "status": "Present"},
        {"student": "Nathi Khoza", "status": "Present"},
        {"student": "Gift Mkansi", "status": "Present"},
        {"student": "Walker  Sibuyi", "status": "Present"},
       
    ]
    
    # Check for download requests
    download = request.GET.get("download")
    download_type = request.GET.get("type")
    if download == "csv" and download_type == "grades":
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="grade_data.csv"'
        writer = csv.writer(response)
        writer.writerow(["Student", "Grade"])
        for record in grade_list:
            writer.writerow([record["student"], record["grade"]])
        return response
    elif download == "csv" and download_type == "attendance":
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="attendance_data.csv"'
        writer = csv.writer(response)
        writer.writerow(["Student", "Status"])
        for record in attendance_list:
            writer.writerow([record["student"], record["status"]])
        return response
    elif download == "pdf":
        # Placeholder for PDF export.
        return HttpResponse("PDF export is not implemented yet.", content_type="text/plain")
    
    
    context = {
        "teacher": {
            "name": "N Mkansi",
            "profile_pic": "dashboard/styles/nyiko.jpg",
            "class": "Computer Science Lecture",
        },
        "attendance_data": attendance_list,
        "grade_data": grade_list,   
        "analytics": {
      
            "chart_data": [78,85,85,45],
        },
        "extra_help_students": [
            {"student": "Jane Roe", "remark": "Struggling with foundational concepts."},
            {"student": "Tom Ray", "remark": "Needs assistance in advanced topics."},
        ],
       
        "average_grade": 78,
        "pass_rate": 85,
        "grade_distribution": [40, 30, 20, 10],
        # Data for the Performance Trends chart
        "performance_trends": {
            "labels": ["Clast Test 1", "Clast Test 2", "Semester Test 1", "Semester Test 2"],
            "data": [75, 78, 80, 30],
        },
    }
    return render(request, "dashboard/teacher_dashboard.html", context)





def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            role = form.cleaned_data.get("role")  # Capturing user role

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                
                # Redirect based on role
                if role == "student":
                    return redirect("student_dashboard")
                elif role == "lecturer":
                    return redirect("lecturer_dashboard")
                elif role == "admin":
                    return redirect("admin_dashboard")
            else:
                form.add_error(None, "Invalid username or password.")

    else:
        form = LoginForm()

    return render(request, "login/login.html", {"form": form})



"""

# add_student view 
def add_student(request):
    if request.method == "POST":
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)

            student.username = student.Email  
             #  Temporary password
            student.password = make_password(student.LastName) 
            student.save()

            #  Assign student role
            student_group, created = Group.objects.get_or_create(name="Students")
            student.groups.add(student_group)

            return redirect("success_page")   
    else:
        form = StudentRegisterForm()

    return render(request, "Home/add_student.html", {"form": form})


# add_lecturer view 
def add_lecturer(request):
    if request.method == "POST":
        form = LecturerRegisterForm(request.POST)
        if form.is_valid():
            lecturer = form.save(commit=False)

            lecturer.username = lecturer.Email   
            lecturer.password = make_password(lecturer.LastName)  
            lecturer.save()

            #  Assign lecturer role
            lecturer_group, created = Group.objects.get_or_create(name="Lecturers")
            lecturer.groups.add(lecturer_group)

            return redirect("success_page")   
    else:
        form = LecturerRegisterForm()

    return render(request, "Home/add_lecturer.html", {"form": form})

"""
