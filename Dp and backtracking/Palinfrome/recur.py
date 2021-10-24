import time
def palindrome(x,i,j):
    if i>=j:
        return True
    if x[i]!=x[j]:
        return False
    return palindrome(x,i+1,j-1)
def main():
    x=input()
    res=palindrome(x,0,len(x)-1)
    print(res)

if __name__=='__main__':
    itime=time.time()
    main()
    print("Time taken is ",time.time()-itime)