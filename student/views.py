from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from disability.models import Disability
from student.forms import StudentForm

from student.models import Sex, Student
from university.models import University

# Create your views here.
def get_student(id):
    try:
        return Student.objects.get(student_id = id)
    except:
        return None

@login_required
def students(request):
    students = Student.objects.all()
    return render(request, 'students.html', {
        'title': 'Estudiantes',
        'panel': 'Estudiantes',
        'students': students
    })

@login_required
def delete_student(request, id):
    student = get_student(id)
    if student:
        student.delete()
        return redirect('students')
    else:
        return render(request, 'error.html', {
            'title': 'Error',
            'message': 'El estudiante no existe.'
        })

@login_required
def edit_student(request, id):
    student = get_student(id)
    if not student:
        return render(request, 'error.html', {
            'title': 'Error',
            'message': 'El estudiante no existe.'
        })

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student.age = form.cleaned_data['age']
            student.start_year = form.cleaned_data['admission_year']
            student.sex = form.cleaned_data['gender']
            student.university = form.cleaned_data['university']
            student.disability = form.cleaned_data['disability']
            student.save()
            return redirect('students')
    else:
        form = StudentForm(initial={
            'age': student.age,
            'admission_year': student.start_year,
            'gender': student.sex,
            'university': student.university,
            'disability': student.disability
        })
        
    return render(request, 'editstudent.html', {
        'title': 'Editar estudiante',
        'form': form,
        'student_id': student.student_id
    })

@login_required
def create_student(request):
    if request.method== 'POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            age=form.cleaned_data['age']
            start_year=form.cleaned_data['admission_year']
            sex = Sex.objects.get(id_sex=form.cleaned_data['gender'].id_sex)
            university = University.objects.get(code=form.cleaned_data['university'].code)
            disability = Disability.objects.get(disability_id=form.cleaned_data['disability'].disability_id)
            Student.objects.create(age=age, start_year=start_year, sex=sex, university=university, disability=disability)
            return redirect('students')
    else:
        form=StudentForm() 
    return render(request, 'createstudent.html', {
        'title': 'Agregar estudiante',
        'form': form
    })