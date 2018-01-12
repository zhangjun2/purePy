# -*- coding:utf-8 -*-
_author__ = 'ZHANGJUN'


class Person(object):
	def __str__(self):
		return self.name

	def __init__(self, name):
		self.__name = name
		super().__init__()

	def getname(self):
		return self.__name

p = Person('zhangjun')
print(p.__getattribute__('_Person__name'))
print(p.getname())

class man:
	def __init__(self):
		pass

m = man()
