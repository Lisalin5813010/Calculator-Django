
from datetime import datetime
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from calculator.models import DiaryItem
aString= ['calculator','people','chart','todoapp','exampleView','logout']
message="Welcome to the Diary App"

class ExampleView(TemplateView, LoginRequiredMixin):
    
    template_name = "calculator/extendedhtml/exampleView.html"
    def get(self, request):
      message="Welcome to the Diary App"
      all_diary_items = DiaryItem.objects.all()
      context = {'aString': aString,'all_diary_items':all_diary_items,'message':message}
      return render(request, self.template_name,context)
    
    def post(self, request):
      all_diary_items = DiaryItem.objects.all()
      if request.POST['paragraphText']:
         text = request.POST['paragraphText']
         new_diary = DiaryItem(content=text)
         new_diary.save()
         context = {'aString': aString,'new_diary':new_diary, 'all_diary_items':all_diary_items, 'message':message}
      else:
         return redirect('exampleView')
      return render(request, self.template_name,context)
    
    
       
      
