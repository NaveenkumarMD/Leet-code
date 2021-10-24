arr=[]
for i in range(10):
    arr.append(bin(i).count("1"))
print(arr)