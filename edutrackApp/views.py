from django.shortcuts import redirect, render
from .models import *
from .forms import *
 

# Create Add Student view 
def add_student_view(request):
    if request.method=='POST':
     form=StudentForm(request.POST)

     if form.is_valid():
        form.save()
        return redirect('list')

    else:
       form=StudentForm()

    return render(request,'add.html',{'form':form})


def students_list_view(request):
    students=Student.objects.all()
    return render(request, 'list.html',{'students':students})


def update_student_view(request,pk):
    student=Student.objects.get(StudentNumber= pk)
    if request.method=='POST':
       form=StudentForm(request.POST,instance=student)

       if form.is_valid():
          form.save()
          return redirect('list')

    else :      
      form=StudentForm(instance=student)
    return render(request, 'update.html',{'form':form})


def delete_student_view(request, pk):
    student=Student.objects.get(StudentNumber=pk)
    if request.method=='POST':
        student.delete()
        return redirect('list')
    




# Create Add Lecture  view 
def add_lecture_view(request):
    if request.method=='POST':
     form=LecturerForm(request.POST)

     if form.is_valid():
        form.save()
        return redirect('lecture_view/list')

    else:
       form=LecturerForm()

    return render(request,'lecture_view/add.html',{'form':form})


def lecture_list_view(request):
    lecturers=Lecturer.objects.all()
    return render(request, 'lecture_view/list.html',{'lecturers':lecturers})


def update_lecture_view(request,pk):
    lecturer=Lecturer.objects.get(StaffNumber= pk)
    if request.method=='POST':
       form=LecturerForm(request.POST,instance=lecturer)

       if form.is_valid():
          form.save()
          return redirect('lecture_view/list')

    else :      
      form=LecturerForm(instance=lecturer)
    return render(request, 'lecture_view/update.html',{'form':form})


def delete_lecture_view(request, pk):
    lecture=Lecturer.objects.get(StaffNumber=pk)
    if request.method=='POST':
        lecture.delete()
        return redirect('lecture_view/list')   



def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'add_department.html', {'form': form})

def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm()
    return render(request, 'add_subject.html', {'form': form})


def subject_list_view(request):
    subjects = Subject.objects.select_related('DepartmentCode').all()
    return render(request, 'subject_list.html', {'subjects': subjects})



