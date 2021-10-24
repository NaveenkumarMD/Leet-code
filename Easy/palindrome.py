def isPalindrome(self, x):
    if(x<0):return False
    l=x
    c=0
    while(x!=0):
        c=c*10+x%10
        x//=10
    print(c)
    return c==l