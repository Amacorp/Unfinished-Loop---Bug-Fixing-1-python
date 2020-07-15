def create_array(n):
    res=[]
    i=1
    while i<=n:
        res+=[i]
        i+= 1
    return res
    
    
OR


def create_array(n):
    return [i for i in range(1,n+1)]
