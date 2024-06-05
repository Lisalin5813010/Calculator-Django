
from django.shortcuts import render, redirect, get_object_or_404
from calculator.views import People
from .models import Student
from django.db import connection
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin

aString= ['calculator','people','chart','todoapp','exampleView','logout']

class PersonView(People):
  def get(self,request):
    students_list = list(Student.objects.all().values('id', 'student_name', 'student_age', 'student_gender'))
    students = Student.objects.all()
    context = {'aString': aString,'students_list': students_list, 'students': students}
    
    return render(request, self.template_name, context)


  def post(self,request):
    
    name = request.POST.get('name')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    if not name or not age or not gender:
       return JsonResponse({'error': 'All fields are required'}, status=400)
    Student.objects.create(student_name=name, student_age=age, student_gender=gender)
    return redirect('people')
        
        # Process the data (e.g., save to database)
        
    response = {
      'status': 'success',
      'message': 'Registration successful!'
    }
    
    return redirect('people')
   
    #return redirect('people')
    


  def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('people')
    students = Student.objects.all()
    return render(request, 'calculator/extendedhtml/insert_data.html', {'students': students})