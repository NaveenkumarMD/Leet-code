import time

def rev(name,i):
    if i==0:
        return name[0]
    else:
        return name[i]+rev(name,i-1)
    
def main():
    x=rev("naveen",5)
    print(x)

if __name__=='__main__':
    itime=time.time()
    main()
    print("Time taken is ",time.time()-itime)