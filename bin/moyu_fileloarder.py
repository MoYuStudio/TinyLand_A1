
import os
import time
import random

class MoYuFileLoarder:
    def __init__(self,path):
        self.path = path
        self.file_read = open(os.getcwd()+self.path,'r')
        self.file_read_data = self.file_read.read()
        self.file_read.close()
        self.file_read_data = eval(self.file_read_data)

    def read(self):
        pass


a1 = time.time()
# map = [[0 for x in range(0,999,1)]for y in range(0,999,1)]
map = ([random.randint(0,5) for x in range(0,9,1)]for y in range(0,9,1))
a2 = time.time()
print(a2-a1)
print(type(map))
print(map)
print(next(map))
# for i in map:
#     print(i)