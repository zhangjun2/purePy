# -*- coding:utf-8 -*-
_author__ = 'ZHANGJUN'


class Man:
	def __init__(self):
		pass

	def sex(self):
		pass


class Person(object):
	def __str__(self):
		return self.name

	def __init__(self, name):
		self.__name = name
		super().__init__()

	def getname(self):
		return self.__name

	def name(self, name: Man):
		self.__name = name


p = Person('zhangjun')
# p.name(12)
print(p.__getattribute__('_Person__name'))
print(p.getname())

m = Man()
p.name(m)
