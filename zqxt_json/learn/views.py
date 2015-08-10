# -*- coding: utf-8 -*-

##example_1
# from __future__ import unicode_literals
# from django.shortcuts import render
 
# def home(request):
#     List = ['自强学堂', '渲染Json到模板']
#     return render(request, 'home.html', {'List': List})

##example_2
from __future__ import unicode_literals

import json
from django.shortcuts import render

def home(request):
	List = ['自强学堂', '渲染Json到模板']
	Dict = {'site': '自强学堂', 'author': '涂伟忠'}
	return render(request, 'home.html', {
			'List': json.dumps(List),
			'Dict': json.dumps(Dict)
		})