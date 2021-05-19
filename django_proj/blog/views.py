from django.shortcuts import render, redirect
from .forms import lcmForm
import math
from functools import reduce
from .models import  lcm_db
from datetime import datetime
# Create your views here.

def lcm1(request):
	try:
		if request.method == "POST":
			fm = lcmForm(request.POST)
			if fm.is_valid():
				n1 = fm.cleaned_data['num1']
				n2 = fm.cleaned_data['num2']
				return redirect(f'/lcm-of-{n1}-and-{n2}/')
		else:
			fm= lcmForm()
			return render(request,'blog/lcm.html',{'forms':fm})
	except:
	  	return redirect('/lcm-calculator/')

def lcm_func(request,num1,num2):
	
	def prime_factors(n):
	    x = []
	    while n % 2 == 0:
	        x.append(2)
	        n = n / 2
	    for i in range(3,int(math.sqrt(n))+1,2):
	       while n % i== 0:
	            x.append(i)
	            n = n / i
	    if n > 2:
	        x.append(n)
	    return x

	v= []
	gcf1 = math.gcd(int(num1),int(num2))
	mul = int(num1)*int(num2)
	lcm1 = mul//gcf1
	prime = prime_factors(int(num1))
	prime2 = prime_factors(int(num2))
	set1 = list(set(prime_factors(int(num1))))
	set1 = [int(i) for i in set1]
	set1.sort()
	s1 = reduce((lambda x, y: x * y), set1)
	set1 = [str(i) for i in set1]
	set2 = list(set(prime_factors(int(num2))))
	set2 = [int(i) for i in set2]
	set2.sort()
	s2 = reduce((lambda x, y: x * y), set2)
	set2 = [str(i) for i in set2]
	set1 = ','.join(set1)
	set2 = ','.join(set2)
	k = set1+set2
	b = lcm_db(inputEnter=num1+'x'+num2,detailStep=k,finalAnswer=lcm1,slug='/lcm-of-{}-and-{}/'.format(num1,num2),solutionTitle='LCM of {} and {}'.format(num1,num2),date_modified=datetime.now())
	b.save()
	content = {'pf1':set1,'pf2':set2,'s1':s1,'s2':s2,'gcf':gcf1,'num1':num1,'num2':num2,'lcm1':lcm1}
	return render(request,'blog/lcm_func.html',content)	