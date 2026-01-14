def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(7))

def square(x,y=0,z=0):
    if y==0 and z==0:
        z+=x
        y+=1
        return square(x,y,z)
    if y<x:
        z+=x
        y+=1
        return square(x,y,z)
    if x==y:
        return z
print(square())
