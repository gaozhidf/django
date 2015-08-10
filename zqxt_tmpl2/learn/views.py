# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

## example_1
# def home(request):
# 	string = u"我在自强学堂学习Django，用它来建网站"
# 	return render(request, 'home.html', {'string': string})

## example_2
# def home(request):
# 	TutorialList = ["HTML", "CSS", "jQuery", "Django"]
# 	return render(request, 'home.html', {'TutorialList': TutorialList})

## example_3
# def home(request):
# 	info_dict = {'site': u'自强学堂', 'content': u'各项IT技术教程'}
# 	return render(request, 'home.html', {'info_dict': info_dict})

## example_4
def home(request):
	List = map(str, range(100)) #一个长度为100的List
	return render(request, 'home.html', {'List': List})