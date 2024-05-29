from calculator.views import Calculator
from calculator.forms import CalForm
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

aString= ['calculator','people','chart','todoapp','exampleView','logout']
class CalculatorView(Calculator):
    
    def get(self, request):
        print(request.user)
        form = CalForm()
        context = {'form': form, 'aString': aString}
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = CalForm(request.POST)
        if request.POST['num1'] and request.POST['num2']:
            try:
                num1 = float(request.POST['num1'])
                num2 = float(request.POST['num2'])
                context = {'form': form, 'result': self.test(
                    request, num1, num2), 'aString': aString}
                return render(request, self.template_name, context)
            except:
                result = "Please enter a valid number"
                context = {'form': form, 'result': result, 'aString': aString }
                return render(request, self.template_name, context)
        else:

            context = {'form': form,
                       'result': 'Please enter a valid number','aString': aString}
            return render(request, self.template_name, context)

    def test(self, request, num1, num2):
        #form = CalForm(request.POST)
        if 'add' in request.POST:
            result = str(num1 + num2)
        elif 'sub' in request.POST:
            result = str(num1 - num2)
        elif 'mul' in request.POST:
            result = str(num1 * num2)
        elif 'div' in request.POST:
            if num2 != 0:
                result = str(num1 / num2)
            else:
                result = "The denominator is not valid"
        elif 'reset' in request.POST:
            result = ''
        
        return result
