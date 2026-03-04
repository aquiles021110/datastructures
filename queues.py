class queue:
    def __init__(self,size):
        self.queue=[None]*size
        self.front=0
        self.rear=0
        self.size=size
        self.avail=size
    def enqueue(self,item):
        if self.avail==0:
            print('Queue Overflow')
        else:
            self.queue[self.rear]=item
            self.rear=(self.rear+1)%self.size
            self.avail-=1
    def dequeue(self):
        if self.avail==self.size:
            print('Queue Underflow')
        else:
            self.queue[self.front]=None
            self.front=(self.front+1)%self.size
            self.avail+=1
    def peek(self):
        print(self.queue[self.front])
    def getrear(self):
        print(self.queue[self.rear])
    def show(self):
        print(self.queue)

q=queue(5)
q.enqueue('Steve')
q.enqueue('James')
q.peek()
q.getrear()
q.dequeue()
q.peek()
q.show()