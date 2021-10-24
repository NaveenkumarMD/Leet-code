import time

def func(x):
    if x%3!=0 and x!=1 :
        return False
    if x==1:
        return True
    return func(x/3)
    
def main():
    x=func(int(input()))
    print(x)

if __name__=='__main__':
    itime=time.time()
    main()
    print("Time taken is ",time.time()-itime)