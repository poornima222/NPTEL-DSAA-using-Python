#Euclid's Algorithm- 
#1 Suppose d divides both m and n, and m>n
#2 Then m=ad, n=bd
#3 So m-n= ad-bd= (a-b)d
#4 d divides m-n as well!!!
#5 So gcd(m,n)=gcd(n,m-n)

#Simplified Algorithm-
#1 Consider gcd(m,n) with m>n
#2 If n divides m, return n
#3 Otherwise, compute gcd(n,m-n) and return that value

def gcd(m,n):
    #Assume m>=n
    if m<n:
        (m,n)=(n,m) #we reverse the values so that we get our desired condition which is m>n 

    if (m%n)==0:
        return(n)
    else:
        diff=m-n
        return(gcd(max(n,diff),min(n,diff))) #the bigger value goes first
    

#Euclid's Algorithm (WHILE LOOP)
    
def gcd(m,n):
    if m<n: #Assume m>=n
        (m,n)=(n,m)

    while (m%n)!=0: #"!=" is not equal to
        diff=m-n
        (m,n)=(max(n,diff),min(n,diff))

    return(n)


#Euclid's Algorithm (The Right Approach)
#1 Consider gcd(m,n) with m>n
#2 If n divides m, return n
#3 Otherwise, let r=m%n
#4 Return gcd(n,r)

def gcd(m,n):
    if m<n: #Assume m>=n
        (m,n)=(n,m)

    if (m%n)==0:
        return(n)
    else:
        return(gcd(n,m%n)) #the remainder 'm%n' is always less than n