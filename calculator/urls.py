from django.urls import path
from calculator.todoappView import TodoappView
from .chartView import ChartView
from . import views
from .exampleView import ExampleView
from .calculatorView import CalculatorView
from .personView import PersonView
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.sign_in, name='login'),
    path('calculator/', CalculatorView.as_view(), name='calculator'),
    path('register/', views.sign_up, name="register"),
    path('people/', PersonView.as_view(), name='people'),
    path('chart/', ChartView.as_view(), name='chart'),
    path('todoapp/', TodoappView.as_view(), name='todoapp'),
    path('exampleview/', ExampleView.as_view(), name='exampleView'),
    path('delete/<int:pk>/',
         TodoappView.delete, name='delete'),
    path('logout/', views.sign_out, name='logout'),
    path('login/', views.sign_in, name='login'),
    path('todoapp/', TodoappView.as_view(), name='cancel'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
