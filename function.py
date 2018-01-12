# -*- coding:utf-8 -*-
import json
from _ctypes_test import func
from functools import reduce
from symbol import decorator

_author__ = 'ZHANGJUN'


# 高级函数

# -------------map函数-------
# map()函数接收两个参数，一个是函数，一个iterable, map()函数将参数的函数作用于iterable的每一个元素，结果是返回新的iterable
def test_map():
	l = map(abs, [1, -3, 3, -6, -7])  # 将序列的元素取绝对值
	print(list(l))


# reduce()函数也是接受两个参数，一个是函数，一个是序列，这个函数必须传入两个参数，reduce把函数作用于序列，并将结果与序列下一个元素做累积计算，
# 比如求和
def test_reduce():
	def f(x, y):
		return x + y

	a = reduce(f, range(100))
	print(a)


# 将一个序列转换成数学数字
def test_reduce2():
	def f(x, y):
		return x * 10 + y

	l = [1, 3, 4, 6, 4, 9]
	print(reduce(f, l))


# filter()函数，接收一个函数和一个序列，将函数作用于序列的每个元素，根据函数返回结果True或者False保留序列该元素，得到新的序列
# 相当于是对序列的元素利用传入的函数做过滤，得到满足函数条件的元素形成的新序列
def test_filter():  # 例：过滤序列中的偶数
	def f(x):
		return x % 2 == 0

	print(list(filter(f, [1, 2, 5, 7, 6, 28])))


# 匿名函数
def test_lamada():
	f = lambda x, y: x + y
	# print(list(map(f, [(1, 2), (4, 5)])))
	print(f(1, 3))


# def log(text):
#
# 	def decorator(func):
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator


if __name__ == '__main__':
	# test_reduce()
	# test_reduce2()
	# test_filter()
	test_lamada()
	# no_repeat_num()
