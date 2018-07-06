# -*- coding: utf-8 -*-
import threading
import time

from werkzeug.local import Local, LocalStack

my_obj = Local()
my_obj.b = 1


def worker():
    my_obj.b = 2
    print("in new thread b is :{}".format(my_obj.b))


new_thread = threading.Thread(target=worker)
new_thread.start()
time.sleep(1)
print("in main thread b is :{}".format(my_obj.b))

s = LocalStack()
s.push(1)
print(s.pop())
print(s.pop())
print(s.top)
