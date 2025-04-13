from django.shortcuts import redirect, render
from .forms import StudentForm
from .models import Student

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