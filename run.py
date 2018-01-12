# -*- coding:utf-8 -*-
import json
import warnings
from imp import reload

import sys
import xlrd

_author__ = 'ZHANGJUN'

import os
import win32com.client as win32
# generator生成杨辉三角
def triangle(lines):
	L = [1]
	n = 1
	while n < lines:
		yield L
		L = [(L[x] + L[x + 1]) for x in range(len(L) - 1)]  # 列表生成式
		L.insert(0, 1)
		L.append(1)
		n = n + 1


def log(func):
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		print(args)  # a tuple
		print(kw)  # a dict
		return func(*args, **kw)

	return wrapper


@log
def add(x, y):
	return x + y


def file(path):
	with open('D:/soft/test.txt', 'r') as f:
		print(f.readlines())


def dirte():
	pylist = [x for x in os.listdir('D:/Users/zhangjun693/PycharmProjects') if
	          os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
	print(pylist)


# --------没有重复数字的三位数
def no_repeat_num():
	l = range(10)
	count = 0
	for a in l[1:]:
		for b in l:
			if a == b: continue  # continue关键字，结束本次循环，继续下次循环
			for c in l:
				if c != b and c != a:
					print(a * 100 + 10 * b + c)
					count += 1
	print('总共有%d个没有重复数字的三位数' % count)


# 水仙花数是指一个n位数（n≥3），它的每个位上的数字的n次幂之和等于它本身。
# 例如：1^3+5^3+3^3=153。
def num_shuixianhua():
	l = range(10)
	count = 0
	for a in l[1:]:
		for b in l:
			for c in l:
				if a * a * a + b * b * b + c * c * c == a * 100 + b * 10 + c:
					print('水仙花数：', a * 100 + b * 10 + c)
					count += 1
	print('总共有%d个水仙花数' % count)


# 方法二相对简单一点，将三位数拆分，然后计算
def num_shuixianhua_2():
	count = 0
	for num in range(100, 1000):
		a = num // 100
		b = num % 100 // 10
		c = num % 10
		if a ** 3 + b ** 3 + c ** 3 == num:
			print('水仙花数：', num)
			count += 1
	print('总共有%d个水仙花数' % count)


# 读取json文件
def read_json():
	with open('D:\soft\data.json', 'r') as f:
		data = json.load(f)
		print(type(data))
	return data


# 完全数（Perfect number)，又称完美数或完备数，是一些特殊的自然数。它所有的真因子(即除了自身以外的约数）的和（即因子函数），
# 恰好等于它本身。例如，第一个完全数是6，它有约数1、2、3、6，除去它本身6外，其余3个数相加，1+2+3=6。
# 第二个完全数是28，它有约数1、2、4、7、14、28，除去它本身28外，其余5个数相加，1+2+4+7+14=28。
# 编程求10000以内的完全数。
def wanquanshu():
	for x in range(1, 10000):
		if sum([a for a in range(1, x) if x % a == 0]) == x:
			print(x)


# 220的真因数之和为1+2+4+5+10+11+20+22+44+55+110=284
# 284的真因数之和为1+2+4+71+142=220
# 毕达哥拉斯把这样的数对A、B称为相亲数：A的真因数之和为B，而B的真因数之和为A。
# 求100000以内的相亲数。
def xiangqinshu():
	num_set = ()
	num_list = []
	for x in range(1, 10000):
		a = sum([i for i in range(1, x) if x % i == 0])
		b = sum([i for i in range(1, a) if a % i == 0])
		if x == b and x != a:
			num_list.append({x, a})
			print(x, a)
	print(num_list)


# 将对象以json格式写入文件 json.dump()函数
def json_test():
	dict_jsonn = dict()
	for x in range(10):
		dict_jsonn[str(x)] = x
	city = [{'name': '北京', 'city': []}, {'name': '湖北', 'city': [{'name': '武汉'}, {'name': '咸宁'}]}]
	with open('D:\soft\\test.txt', 'w') as f:
		json.dump(city, f, sort_keys=True, indent=4, ensure_ascii=False)  # ensure_ascii=False可以使数据中的中文正常写入文件，正常显示

	with open('D:\soft\\test.txt', 'r')as f:
		data = json.load(f)
		print(data)


class Student:
	def __init__(self, id, name, age):
		self.id = id
		self.name = name
		self.age = age


def dict2Student(d):
	return Student(d['id'], d['name'], d['age'])


# 对象转json， Json转对象
def obj_convert_json():
	stu = Student('11111', '张军', 20)
	# 类对象转成Json两种方法，第一种利用default参数，default = lambda obj: obj.__dict__,意思是将传进来的第一个参数obj通过匿名函数转换成dict字典
	# json_value = json.dumps(stu, default=lambda
	# 	obj: obj.__dict__, ensure_ascii=False, sort_keys=True, indent=4)
	# 第二种方式，第一个参数传obj.__dict__,对象的属性字典对象。
	json_value = json.dumps(stu.__dict__, ensure_ascii=False, sort_keys=True, indent=4)

	print(json_value)
	t = '{"age": 20,"id": "11111","name": "张军"}'
	print(json.loads(t, object_hook=dict2Student))


def send_outlook():
	outlook = win32.Dispatch('outlook.application')
	mail = outlook.CreateItem(0)
	receivers = ['xuxunxiong954@pingan.com.cn']
	mail.To = receivers[0]
	mail.Subject = 'test1'
	workbook = xlrd.open_workbook('E:\\kpi excel\\00_summary.xls')
	mySheet = workbook.sheet_by_index(0)

	nrows = mySheet.nrows
	content = []
	for i in range(nrows):
		ss = mySheet.row_values(i)
		content.append(ss)
		print(content)
		Truecontent = str(content)

	mail.Body = Truecontent
	# mail.Attachments.Add('E:\\kpi excel\\00_summary.xls')
	mail.Send()


def send_email(sub, body):
	outlook = win32.Dispatch('outlook.application')
	# outlook = win32.gencache.EnsureDispatch('Outlook.Applicatioin')
	receivers = ['XUXUNXIONG954@pingan.com.cn']
	mail = outlook.CreateItem(0)
	# mail = outlook.CreateItem(win32.constants.olMailItem)
	mail.To = 'XUXUNXIONG954@pingan.com.cn'
	mail.Subject = sub
	mail.Body = body
	# 添加附件
	# mail.Attachments.Add('D:\Users\xxx\Desktop\email.log')
	mail.Send()
	print('ok')


reload(sys)
# sys.setdefaultencoding('utf8')
# warnings.filterwarnings('ignore')

if __name__ == '__main__':
	# l = [(x * x) for x in range(100) if x % 3 == 0]
	# print(l)
	# g = list(map(triangle, range(10)))
	# for j in g:
	# 	for x in j:
	# 		print(x)
	# 	print("---------------------------")
	# add(3, 4)
	# print(j)
	# o = triangle(20)
	# for x in o:
	# 	print(x)
	# # file('D:\soft\test.txt')
	# dirte()
	# read_json()
	# wanquanshu()
	# xiangqinshu()
	# json_test()
	# obj_convert_json()
	send_email('aaacx,u', 'fff')
	# send_outlook()











# ---------测试Mysql连接,数据库操作
# result = mydb.execute_query('select * from t_address_info')
# print(result)
