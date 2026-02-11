def merge(left,right):
    res=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    res.extend(left[i:])
    res.extend(right[j:])
    return res
def mergesort(a):
    if len(a)<=1:
        return a
    mid=len(a)//2
    left=mergesort(a[:mid])
    right=mergesort(a[mid:])
    return merge(left,right)

array=[4,3,5,2]
print(mergesort(array))
array2=[321,33,23,500,44,23]
def bigmerge(left,right):
    res=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]>right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    res.extend(left[i:])
    res.extend(right[j:])
    return res
def bigmergesort(a):
    if len(a)<=1:
        return a
    mid=len(a)//2
    left=bigmergesort(a[:mid])
    right=bigmergesort(a[mid:])
    return bigmerge(left,right)
print(bigmergesort(array2))
