import time

def fib(n):
    if n==1:
        return 1
    if n==0:
        return 0
    else:
        return fib(n-1)+fib(n-2)
def main():
    print(fib(50))

if __name__=='__main__':
    itime=time.time()
    main()
    print("Time taken is ",time.time()-itime)