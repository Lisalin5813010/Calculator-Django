from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from calculator.views import Todoapp
from django.contrib import messages
from .models import TodoListItem
aString= ['calculator','people','chart','todoapp','exampleView','logout']
class TodoappView(Todoapp):
    
    def get(self, request):
      all_todo_items = TodoListItem.objects.all()
      context = {'all_todo_items': all_todo_items, 'aString': aString}
      return render(request, self.template_name, context)
   
    def post(self, request):
        all_todo_items = TodoListItem.objects.all()
        context = {'aString': aString,'all_todo_items':all_todo_items}
        query = request.POST.get('query', '')
        print(query)
        content = request.POST.get('content', '')
        print(content)
        if query:
          # Filter items where content contains the query
          all_items = TodoListItem.objects.filter(content__icontains=query)
          if all_items.count != 0:
            message = "Found " + str(all_items.count()) + " items"
            context = {'message': message, 'aString': aString,'all_todo_items':all_todo_items}
          else:
            message = "No items found"
            context = {'message': message, 'aString': aString,'all_todo_items':all_todo_items}
        else:
          if content:
            new_item = TodoListItem(content=content)
            new_item.save()
            context = {'new_item': new_item, 'aString': aString,'all_todo_items':all_todo_items}
          else:
             redirect('todoapp')
        return render(request, self.template_name, context)
    
       
    

    @login_required
    def editTodoView(self, request, pk):
        y = get_object_or_404(TodoListItem, pk=pk)
        context = {"y": y}
        if request.method == 'GET':
            return render(request, self.template_name, context)

    @login_required
    def delete(request, pk):
        all_todo_items = TodoListItem.objects.all()
        y = get_object_or_404(TodoListItem, pk=pk)
        context = {"y": y, 'aString': aString,'all_todo_items':all_todo_items}
        if request.method == 'GET':
            return render(request, "calculator/post_confirm_delete.html", context)
        elif request.method == 'POST':
            y.delete()
            return redirect('todoapp')
        
            
        
    
      
