#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading

_author__ = 'ZHANGJUN'


# 因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，必须先获得GIL锁，
# 然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，
# 所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。
# GIL是Python解释器设计的历史遗留问题，通常我们用的解释器是官方实现的CPython，要真正利用多核，除非重写一个不带GIL的解释器。
# 所以，在Python中，可以使用多线程，但不要指望能有效利用多核。如果一定要通过多线程利用多核，那只能通过C扩展来实现，不过这样就失去了Python简单易用的特点。
# 不过，也不用过于担心，Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响。
lock = threading.Lock()

n = 0


def loop(arg):
	for i in range(100):
		change(arg)


def change(arg):
	global n
	n = n + arg
	n = n - arg


def loop2():
	global n
	print('the current thread is %s' % threading.current_thread().name)
	while n > 0:
		n -= 1
		print('thread %s n is %d' % (threading.current_thread().name, n))
	print('the %s thread ended' % threading.current_thread().name)


if __name__ == '__main__':
	t1 = threading.Thread(target=loop, args=(5,))
	t2 = threading.Thread(target=loop, args=(8,))
	t1.start()
	t2.start()
	# t1.join()
	# t2.join()
	# print('the %s thread is ended' % threading.current_thread().name)
	print(n)