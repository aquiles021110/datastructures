def bubblesort(a):
    n=len(a)
    for i in range(n):
        swap=False
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                swap=True
                a[j],a[j+1]=a[j+1],a[j]
        if not swap:
            break
    return a
array=[231,343,567,12,35,504,711,21,14,52,47,222,111,121,144]
print(bubblesort(array))
#swaps values adjacent to it to sort
#time complexity : O(n);O(n²)
#space complexity : O(1)
def l_bubblesort(a):
    n=len(a)
    for i in range(n):
        swap=False
        for j in range(0,n-i-1):
            if a[j]<a[j+1]:
                swap=True
                a[j],a[j+1]=a[j+1],a[j]
        if not swap:
            break
    return a
print(l_bubblesort(array))


def insertionsort(a):
    for i in range(1,len(a)):
        key=a[i]
        j=i-1
        while j>=0 and key<a[j]:
            a[j+1]=a[j]
            j-=1
        a[j+1]=key
    return a
        
a=[8,3,5,2,1,42]
print(insertionsort(a))
