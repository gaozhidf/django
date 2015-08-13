# # coding:utf-8
##example_1
# from django.db import models

# # Create your models here.

# class Article(models.Model):
# 	title = models.CharField(u'标题', max_length=256)
# 	content = models.TextField(u'内容')

# 	pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
# 	update_time = models.DateTimeField(u'更新时间',auto_now=True, null=True)
	
# 	def __unicode__(self):	# 在Python3中用 __str__ 代替 __unicode__
# 		return self.title


# coding:utf-8
##example_2
from __future__ import unicode_literals
##可用于python2.x和python3.x的兼容
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Article(models.Model):
	title = models.CharField('标题', max_length=256)
	content = models.TextField('内容')

	pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable = True)
	update_time = models.DateTimeField('更新时间', auto_now=True, null=True)

	def __str__(self):
		return self.title

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
 
    def my_property(self):
        return self.first_name + ' ' + self.last_name
    my_property.short_description = "Full name of the person"
 
    full_name = property(my_property)

    def __str__(self):
		return self.first_name