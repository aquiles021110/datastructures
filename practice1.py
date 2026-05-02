# def countdown(n):
#     if n<=0:
#         return
#     else:
#         print(n)
#         countdown(n-1)
# countdown(5)
###
#print('NEXT EX0')
###
# def root(x):
#     lo=0
#     hi=x
#     while lo<=hi:
#         mid=(lo+hi)//2
#         if mid*mid==x:
#             return mid
#         elif mid*mid<x:
#             lo=mid+1
#         elif mid*mid>x:
#             hi=mid-1
# print(root(49))
###
'''print('NEXT EX0')'''
###
#insertion sort
list=["apple", "kiwi", "banana", "pie", "date"]
print(list)
def sortlen(list):
    for i in range(1,len(list)):
        temp=list[i]
        prev=i-1
        while prev>=0 and len(temp)<len(list[prev]):
            list[prev+1]=list[prev]
            prev-=1
        list[prev+1]=temp
    print(list)
sortlen(list)