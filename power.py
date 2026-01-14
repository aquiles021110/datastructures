def power(x,y):
    if y==1:
        return x
    else:
        if y%2==0:
            return (power(x,y//2)*power(x,y//2))
        else:
            return (x*power(x,y//2)*power(x,y//2))
print(power(7,2))