'''def Bulle(T):
    N=len(T)
    for i in range (N-1,0,-1):
        for j in range (0,i):
            if T[j]>T[j+1]:
                T[j],T[j+1]=T[j+1],T[j]
    return T

def selection(T):
    N=len(T)
    for i in range (0,N-1):
        m=i
        for j in range (i+1,N):
            if T[j]<T[m]:
                m=j
        if m!=i:
            T[i],T[m]=T[m],T[i]
    return T

def insertion (T):
    N=len(T)
    for i in range(1,N):
        x=T[i]
        pos=i
        for j in range(i-1,-1,-1):
            if x < T[j]:
                pos=j
        for k in range(i,pos,-1):
            T[k]=T[k-1]
        T[pos]=x
    return T'''


def Chercherelt(L,a):
    n=len(L)
    i=0
    while i<n and L[i]!=a :
        i=i+1
    if i<n :
        return True
    else:
        return False


    
