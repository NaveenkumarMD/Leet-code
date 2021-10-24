import time

def func(x):
    if x<=1:
        return x
    return x%2+func(x//2)*10
def main():
    x=int(input())
    res=func(x)
    print(res)

if __name__=='__main__':
    itime=time.time()
    main()
    print("Time taken is ",time.time()-itime)