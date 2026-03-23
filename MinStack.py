class MinStack(object):

    def __init__(self):
        self.s = []
        self.ms = []

    def push(self, val):
        self.s.append(val)
        if not self.ms or val <= self.ms[-1]:
            self.ms.append(val)

    def pop(self):
        if self.s:
            v = self.s.pop()
            if self.ms and v == self.ms[-1]:
                self.ms.pop()

    def top(self):
        return self.s[-1] if self.s else -1

    def getMin(self):
        return self.ms[-1] if self.ms else -1