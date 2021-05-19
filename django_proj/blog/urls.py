from django.urls import path
from . import views

urlpatterns = [
    path('lcm-calculator/',views.lcm1,name='lcm1'),
    path('lcm-of-<str:num1>-and-<str:num2>/',views.lcm_func,name='lcm_func'),
]
