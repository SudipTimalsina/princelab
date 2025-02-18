# student/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

# CREATE operation: Add a new Student
def student_create_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student-list')  # Redirect to list after creation
    else:
        form = StudentForm()

    return render(request, 'student/student_form.html', {'form': form})

# READ operation: List all Students
def student_list_view(request):
    students = Student.objects.all()  # Fetch all students
    return render(request, 'student/student_list.html', {'students': students})

# READ operation: View details of a specific Student
def student_detail_view(request, id):
    student = get_object_or_404(Student, id=id)  # Fetch student by primary key
    return render(request, 'student/student_detail.html', {'student': student})

# UPDATE operation: Edit an existing Student
def student_update_view(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student-detail', id=id)  # Redirect to detail after update
    else:
        form = StudentForm(instance=student)

    return render(request, 'student/student_form.html', {'form': form})

# DELETE operation: Remove a Student
def student_delete_view(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('student-list')  # Redirect to list after deletion

    return render(request, 'student/student_confirm_delete.html', {'student': student})
