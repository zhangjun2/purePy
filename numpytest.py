# -*- coding:utf-8 -*-
_author__ = 'ZHANGJUN'

import numpy as np

# a = [1, 2, 3, 4]
# b = np.array(a)
#
# print(b.shape)
# c =np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# print(c)
# print(c[0][0][0])

from datetime import date

from datetime import datetime
# from datetime import time
import time

# now = datetime.now()  # 日期时间

now = date.today()  # 日期

nowdate = date.fromtimestamp(time.time())

print(now)
print(now.toordinal())
print(nowdate)
print(time.localtime())

print(date.fromordinal(736713))
# 输出结果：2018-01-19

birthday = date(1992, 1, 17)
age = nowdate - birthday
print(age.days)

