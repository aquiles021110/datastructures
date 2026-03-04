def reverse(s):
    stack=[]
    reverse=''
    for i in s:
        stack.append(i)
    while stack:
        reverse+=stack.pop()
    print(reverse)
reverse('PYHTHON')