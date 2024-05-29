
from django.shortcuts import render
from calculator.views import People


class PersonView(People):
  def get(self,request):
    data_list = [
        {'name': 'John', 'age': 30},
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 35},
    ]
    aString= ['calculator','people','chart','todoapp','exampleView','logout']
    context = {'data_list': data_list, 'aString': aString}
    return render(request, self.template_name, context)
  