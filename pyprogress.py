import random
import time
import sys

class UpdateError(Exception):
    pass

class bar(object):
    def __init__(self, count, width=50):
        self.amount = 0
        self.width = width
        self.count = count
        self.done = 0
        sys.stdout.write('[%s]'%(' '*self.width))
        sys.stdout.flush()
        sys.stdout.write('\b'*(self.width+1))

    def update(self):
        if self.done == self.count:
            raise UpdateError('too much updates!')
        self.amount %= self.count
        self.amount += self.width
        self.length = self.amount // self.count
        if self.length > 1:
            self.done += 1
        sys.stdout.write('-'*self.length)
        if self.done == self.count:
            sys.stdout.write('\n')
        sys.stdout.flush()
