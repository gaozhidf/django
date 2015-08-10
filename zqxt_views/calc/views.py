from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

##example_1
# def add(request):
# 	a = request.GET['a']
# 	b = request.GET['b']
# 	c = int(a) + int(b)
# 	return HttpResponse(str(c))

##example_2
# def add2(request, a, b):
# 	c = int(a) + int(b)
# 	return HttpResponse(str(c))

##example_3
def add(request, a, b):
	return render(request, 'home.html')