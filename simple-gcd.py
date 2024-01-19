#defining a function "gcd" with variables "m" and "n"
def gcd(m,n):
    #defining a list "fm" within "gcd" ([]- represents an empty list)
    fm=[]
    #declaring an integer "i" in the range "1,m+1", which is mathematically a range from 1 and upto m+1 (does NOT include m+1)
    for i in range(1,m+1):
        #here % is the remainder function, which means we're defining a condition where when m is divided by i, the remainder is zero 
        if (m%i) == 0:
            #here the function "append" adds the variable "i" to the list "fm", "append" typically in english means adding to the end of the list
            fm.append(i)

    #following the same process to create "fn"
    fn=[]
    for j in range(1,n+1):
        if (n%j) == 0:
            fn.append(j)

    #creating a list of common factors
    cf=[]
    #for every factor in "fm", that also appears in "fn":
    for f in fm:
        if f in fn:
            #we append that factor to "cf"
            cf.append(f)

    #the function below returns the -1th element of "cf", ie. returns the RIGHTMOST element
    return(cf[-1])