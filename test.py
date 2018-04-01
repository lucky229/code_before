# -*- coding:utf-8 -*-

from multiprocessing import Pool
import os, time, random

class abd():
    def a(self, num):
        print('Task %s (%s) running...' % (num, os.getpid()))
        #start = time.time()
        time.sleep(random.random()*3)

        print("Task %s ends." % num)

if __name__ == '__main__':
    print()
    p = Pool(6)
    for i in range(30):
        p.apply_async(abd().a, args=(i, ))
    p.close()
    p.join()
    print('Done')