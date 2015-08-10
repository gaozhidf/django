"""zqxt_views URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin

##example_1
##http://127.0.0.1:8000/add/?a=4&b=5
# urlpatterns = [

#     url(r'^admin/', include(admin.site.urls)),

#     url(r'^add/$', 'calc.views.add', name='add'),

#     #url(r'^add/(\d+)/(\d+)/$', 'calc.views.add2', name='add2'),
# ]

##example_2
##http://127.0.0.1:8000/add/4/5/ 
# urlpatterns = [

#     url(r'^admin/', include(admin.site.urls)),

#     url(r'^add/(\d+)/(\d+)/$', 'calc.views.add2', name='add2'),
# ]


##example_3
##http://127.0.0.1:8000/add/4/5/ 
urlpatterns = patterns('',
    url(r'^add/(\d+)/(\d+)/$', 'calc.views.add', name='add'),
)

##example_3_2
##http://127.0.0.1:8000/jiafa/4/5/ 
# urlpatterns = patterns('',
#     url(r'^jiafa/(\d+)/(\d+)/$', 'calc.views.add', name='add'),
# )