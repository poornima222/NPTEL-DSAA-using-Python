#Iteration One- Eliminating separate lists for m(fm) and n(fn) and directly computing the list of common factors(cf)

def gcd(m,n):
    cf=[]
    for i in range(1,min(m,n)+1):
        if (m%i)==0 and (n%i)==0:
            cf.append(i)

    return(cf[-1])

#Iteration Two- Eliminating the need for lists at all and keeping a single value known as the 'most recent common factor'(mrcf)

def gcd(m,n):
    for i in range(1,min(m,n)+1):
        if (m%1)==0 and (n%1)==0:
            mrcf=i

        return(mrcf)
    
#Iteration Three- Eliminating an ascending list and scanning backwards so that we encounter the greatest value first
    
def gcd(m,n):
    i=min(m,n)
    while i>0:
        if (m%i)==0 and (n%i)==0:
            return(i)
        else:
            i=i-1