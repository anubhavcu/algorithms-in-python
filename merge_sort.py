def merge (A,l,m,r):
    n1=m-l+1
    n2=r-m
    l1=[0]*(n1) # creating 2 list and copying contents of original list
    l2=[0]*(n2)
    for i in range(0,n1):
        l1[i]=A[l+i]
    for j in  range(0,n2):
        l2[j]=A[m+j+1] #since floor is  used to find middle element


    i,j=0,0
    k=l
    '''for k in range(l,r):
        if l1[i]<l2[j]:
            A[k]=l1[i]
            i+=1
        else:
            A[k]=l2[j]
            j+=1
'''
    #comparing and copying back the elements to original list

    while i< n1 and j<n2 :
        if l1[i]<=l2[j]:
            A[k]=l1[i]
            i+=1
        else:
            A[k]=l2[j]
            j+=1
        k+=1
# we can also add infinite at the  end of list to these two loops
    while i<n1:   # copying the remaining elements of left list if any is left
        A[k]=l1[i]
        i+=1
        k+=1
    while j<n2:#copying the remaining elements of right list if any is left
        A[k]=l2[j]
        j+=1
        k+=1
def mergesort(A,l,r):
    if l<r :
        m=(l+(r-1))//2
        mergesort(A,l,m)
        mergesort(A,m+1,r)
        merge(A,l,m,r)

#drivers code to test above algo

print('enter the elements you want to be sorted ')
A=list(map(int,input().split()))
n=len(A)
print(n)
mergesort(A,0,n-1)
print(A)





