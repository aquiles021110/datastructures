class stack:
    def __init__(self,n):
        self.ss=[]
        self.n=n #number of elements
    def push(self,k):
        if len(self.ss)<self.n:
            self.ss.append(k)
        else:
            print('Stack Full')
    def pop(self):
        if len(self.ss)==0:
            print('Stack Empty')
        else:
            self.ss.pop(-1)
    def top(self):
        if len(self.ss)==0:
            print('Stack Empty')
        else:
            return self.ss[-1]
    def size(self):
        return len(self.ss)
    def display(self):
        print(self.ss)
s=stack(5)
s.display()
print(s.size())
s.push(-2)
s.display()
s.push(12)
s.push(2020)
s.push(45)
s.display()
s.pop()
s.display()
print(s.top())
print(s.size())
#time complx=O(n)