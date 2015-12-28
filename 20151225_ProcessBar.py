# coding=utf-8
# 2015年12月25日18:40:33

import sys
import time

class ProcessBar:
    """实现控制台中的进度条"""
    def __init__(self, count=0, total=0, width=50):
        self.count = count
        self.total = total
        self.width = width

    def move(self):
        self.count += 1

    def log(self, s):
        sys.stdout.write(' '*(self.width + 9) + '\r')
        sys.stdout.flush()
        print(s)
        progress = int(self.width * self.count/self.total)
        sys.stdout.write('{0:3}/{1:3}:'.format(self.count, self.total))
        sys.stdout.write('#' * progress + '-'*(self.width-progress) + '\r')
        if progress == self.width:
            sys.stdout.write('\n')
        sys.stdout.flush()

bar = ProcessBar(total=10)
for i in range(10):
    bar.move()
    bar.log("we have arrived at:" + str(i+1))
    time.sleep(1)

print("-----end-----")
print("-----end-----")
print("-----end-----")