import random
import time
import sys

class bar(object):
    def __init__(self, count, width=50):
        self.amount = 0
        self.width = width
        self.count = count
        
    def setup(self):
        sys.stdout.write('[%s]'%(' '*self.width))
        sys.stdout.flush()
        sys.stdout.write('\b'*(self.width+1))

    def update(self):
        self.amount %= self.count
        self.amount += self.width
        sys.stdout.write('-'*(self.amount//self.count))
        sys.stdout.flush()

    def finish(self):
        sys.stdout.write('\n')
