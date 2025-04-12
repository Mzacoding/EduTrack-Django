from django.db import models

class Department(models.Model):
    DepartmentCode = models.CharField(max_length=6, primary_key=True)
    DepartmentName = models.CharField(max_length=100)

    def __str__(self):
        return self.DepartmentName

class Lecturer(models.Model):
    StaffNumber = models.CharField(max_length=9, primary_key=True)
    FirstName = models.CharField(max_length=25)
    LastName = models.CharField(max_length=25)
    Email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"

class Subject(models.Model):
    SubjectCode = models.CharField(max_length=20, primary_key=True)
    SubjectName = models.CharField(max_length=100)
    DepartmentCode = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.SubjectName

class Student(models.Model):
    StudentNumber = models.CharField(max_length=9, primary_key=True)
    FirstName = models.CharField(max_length=25)
    LastName = models.CharField(max_length=25)
    Email = models.EmailField(unique=True)
    contactNumber= models.CharField(max_length=20)


    def __str__(self):
        return f"{self.FirstName} {self.LastName}"
  
class Semester(models.Model):
    SemesterCode = models.CharField(max_length=10, primary_key=True)
    SemesterName = models.CharField(max_length=50)
    StartDate = models.DateField()
    EndDate = models.DateField()

    def __str__(self):
        return self.SemesterName


class Attendance(models.Model):
    AttendId = models.AutoField(primary_key=True)
    StudentNumber = models.ForeignKey(Student, on_delete=models.CASCADE)
    SubjectCode = models.ForeignKey(Subject, on_delete=models.CASCADE)
    DateAndTime = models.DateTimeField(auto_now_add=True)
    Status = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.StudentNumber} - {self.SubjectCode}"

class LecturerCourses(models.Model):
    LecturerCourseId = models.AutoField(primary_key=True)
    StaffNumber = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    SubjectCode = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.StaffNumber} - {self.SubjectCode}"
    
 
class Assessment(models.Model):
    AssessmentCode = models.CharField(max_length=20, primary_key=True)
    AssessmentName = models.CharField(max_length=100)
    TotalMark = models.IntegerField()
    SubjectCode = models.ForeignKey(Subject, on_delete=models.CASCADE)
    StaffNumber = models.ForeignKey(Lecturer, on_delete=models.CASCADE)

    def __str__(self):
        return self.AssessmentName
  
class StudentMarks(models.Model):
    StudentMarkId = models.AutoField(primary_key=True)
    StudentNumber = models.ForeignKey(Student, on_delete=models.CASCADE)
    AssessmentCode = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    MarksObtained = models.IntegerField()

    def __str__(self):
        return f"{self.StudentNumber} - {self.AssessmentCode}"
  
class StudentProgress(models.Model):
    StudentProgressId = models.AutoField(primary_key=True)
    StudentNumber = models.ForeignKey(Student, on_delete=models.CASCADE)
    SubjectCode = models.ForeignKey(Subject, on_delete=models.CASCADE)
    Grade = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.StudentNumber} - {self.SubjectCode}"

class Enrollment(models.Model):
    EnrollmentId = models.AutoField(primary_key=True)
    StudentNumber = models.ForeignKey(Student, on_delete=models.CASCADE)
    SubjectCode = models.ForeignKey(Subject, on_delete=models.CASCADE)
    SemesterCode = models.ForeignKey(Semester, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.StudentNumber} - {self.SubjectCode} - {self.SemesterCode}"
  
class FaceRecognition(models.Model):
    FaceRecognitionId = models.AutoField(primary_key=True)
    StudentNumber = models.ForeignKey(Student, on_delete=models.CASCADE)
    FaceImg = models.BinaryField()

    def __str__(self):
        return f"{self.StudentNumber}"
 
class Admin(models.Model):
    AdminId = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=25)
    LastName = models.CharField(max_length=25)
    Email = models.EmailField(unique=True)
    
    def __str__(self):
        return f"{self.FirstName} {self.LastName}"

class UserLogs(models.Model):
    LogId = models.AutoField(primary_key=True)
    AdminName = models.CharField(max_length=50)
    LogDescription = models.CharField(max_length=100)
    DateAndTime = models.DateTimeField(auto_now_add=True)
    Details = models.TextField()

    def __str__(self):
        return f"{self.AdminName} - {self.LogDescription}"
