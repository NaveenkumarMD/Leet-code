import time
def func(x):
    if x==0:
        return 0
    return x+func(x-1)    
def main():
    x=int(input())
    res=func(x)
    print(res)
if __name__=='__main__':
    itime=time.time()
    main()
    print("Time taken is ",time.time()-itime)