import csv
from django.shortcuts import render, HttpResponse

def student_dashboard(request):
    context = {
        "user": {
            "name": "John Doe",
            "profile_pic": "https://via.placeholder.com/40",  # Placeholder image URL
        },
        "notifications": [
            "Your attendance has been marked.",
            "A new grade has been posted.",
        ],
        "grades": [
            {"course": "Math", "grade": "A"},
            {"course": "Science", "grade": "B+"},
            {"course": "History", "grade": "A-"},
        ],
        "performance_data": [65, 70, 75, 80, 85],  # Sample performance values
    }
    return render(request, "dashboard/student_dashboard.html", context)
 

def admin_dashboard(request):
    context = {
        "admin": {
            "name": "Admin User",
            "profile_pic": "https://via.placeholder.com/40",
        },
        "user_management": [
            {"name": "John Doe", "role": "Student"},
            {"name": "Jane Roe", "role": "Student"},
            {"name": "Ms. Smith", "role": "Teacher"},
        ],
        "report_data": {
            "attendance_percentage": 92,
            "average_grade": "B+",
        },
        "attendance_reports": [
            {"date": "2025-05-01", "present": 100, "absent": 5},
            {"date": "2025-05-02", "present": 98, "absent": 7},
        ],
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
        # ... (more records as needed)
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
        # KPI values for Student Performance Insights
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
