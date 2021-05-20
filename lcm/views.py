from django.shortcuts import render, redirect 
from .forms import LCMForm
import math
from datetime import datetime
from .models import LCM
# Create your views here.
def home(request):
	return redirect('/lcm-calculator/')

def lcm1(request):
	try:
		if request.method == "POST":
			fm = LCMForm(request.POST)
			if fm.is_valid():
				num1 = fm.cleaned_data['num1']
				num2 = fm.cleaned_data['num2']
				def Prime_factor(num):
					l = []
					if num%2==0:
						l.append(2)
						num=num//2
					for i in range(3,int(math.sqrt(num))+1,2):
						while num % i== 0:
							l.append(i)
							num = num / i
					if num > 2:
						l.append(num)
					return l
				gcf = math.gcd(num1,num2)
				lcm = (num1*num2)//gcf
				prime_fact1 = Prime_factor(num1)
				prime_fact2 = Prime_factor(num2)
				prime_fact1.sort()
				prime_fact2.sort()
				l = []
				re=True
				for i in prime_fact1:
					if i not in prime_fact2:
						l.append(i)
				for i in prime_fact2:
					l.append(i)
					#reg = LCM(inputs=str(num1)+'x'+str(num2),finalresult=lcm,firstfact=prime_fact1,secondfact=prime_fact2,slug=f'/lcm-of-{num1}-and-{num2}/',lastmodified=datetime.now(),li=l)
					#reg.save()

				context = {'lcm':lcm,'l':l,'prime_fact1':prime_fact1,'prime_fact2':prime_fact2,'num1':num1,'num2':num2,'forms':fm,'re':re}
				return render(request,'lcm/lcm.html',context)
				
		else:
			re = False
			fm= LCMForm()
		return render(request,'lcm/lcm.html',{'forms':fm})
	except:
		return redirect('/lcm-calculator/')
'''
def result(request,num1,num2):
	fm = LCMForm(request.POST)
	re = True
	#if LCM.objects.filter(inputs=str(num1)+'x'+str(num2)).exists():
	#	pi = LCM.objects.filter(inputs=str(num1)+'x'+str(num2))
	#	lcm = pi[0].finalresult
	#	prime_fact1 = pi[0].firstfact
	#	prime_fact2 = pi[0].secondfact
	#	l = pi[0].li
	#	print("From DataBase")
	#elif LCM.objects.filter(inputs=str(num2)+'x'+str(num1)).exists():
	#		pi = LCM.objects.filter(inputs=str(num2)+'x'+str(num1))
	#	lcm = pi[0].finalresult
	#	prime_fact1 = pi[0].firstfact
	#	prime_fact2 = pi[0].secondfact
	#	l = pi[0].li
	#	print("From DataBase")
	#else:
	def Prime_factor(num):
		l = []
		if num%2==0:
			l.append(2)
			num=num//2
		for i in range(3,int(math.sqrt(num))+1,2):
			while num % i== 0:
				l.append(i)
				num = num / i
		if num > 2:
			l.append(num)
		return l
	gcf = math.gcd(num1,num2)
	lcm = (num1*num2)//gcf
	prime_fact1 = Prime_factor(num1)
	prime_fact2 = Prime_factor(num2)
	prime_fact1.sort()
	prime_fact2.sort()
	l = []
	for i in prime_fact1:
		if i not in prime_fact2:
			l.append(i)
	for i in prime_fact2:
		l.append(i)
		#reg = LCM(inputs=str(num1)+'x'+str(num2),finalresult=lcm,firstfact=prime_fact1,secondfact=prime_fact2,slug=f'/lcm-of-{num1}-and-{num2}/',lastmodified=datetime.now(),li=l)
		#reg.save()

	context = {'lcm':lcm,'l':l,'prime_fact1':prime_fact1,'prime_fact2':prime_fact2,'num1':num1,'num2':num2,'forms':fm,'re':re}
	return render(request,'lcm/lcm.html',context)'''



