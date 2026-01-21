#Linearsearch-going one by one
def linearsearch(a,k):
    for i in range(len(a)):
        if a[i]==k:
            return i
    return -1
array=[123,40563,3231,2026,314,600,2026,123,27,28,3231,1414,23,41]
key=2026
print(linearsearch(array,key))
#Time complexity for linear search is O(n), best case is 1
#Space complexity for linear search is O(1), space does not change
def binarysearch(a,k):
    l=0
    h=len(a)-1
    while l<=h:
        m=(l+h)//2
        if a[m]==k:
            return m
        elif k<a[m]:
            h=m-1
        else:
            l=m+1
    return -1
arraysorted=[32,42,79,210,699,2010,2025,4560,20000]
key=20000
print(binarysearch(arraysorted,key))
#average case O(log(n))
#space complexity O(log(n))
#needs sorted data

#smallest element

def small_linearseach(a):
    s=a[0]
    for i in range(len(a)):
        if a[i]<s:
            s=a[i]
    return s
print(small_linearseach(array))

#biggest element

def big_linearsearch(a):
    s=a[-1]
    for i in range(len(a)):
        if a[i]>s:
            s=a[i]
    return s

print(big_linearsearch(array))

#occurences
def linearsearchoccur(a,k):
    s=0
    for i in range(len(a)):
        if a[i]==k:
            s+=1
    return s
print(linearsearchoccur(array,123))
