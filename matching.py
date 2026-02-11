openlist=['[','{','(']
closedlist=[']','}',')']
def check(string):
    stack=[]
    for i in string:
        if i in openlist:
            stack.append(i)
        elif i in closedlist:
            pos=closedlist.index(i)
            if len(stack)>0 and openlist[pos]==stack[len(stack)-1]:
                stack.pop()
            else:
                return 'Unbalenced'
    if len(stack)==0:
        return 'Balenced'
    else:
        return 'Unbalenced'
v='hiprint(this[insidethis{}])'
n='ohno(prints(list?[]]){'
print(check(v))
print(check(n))