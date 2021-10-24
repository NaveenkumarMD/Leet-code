# def check(arr,target):
#     sumx=target
#     for i in range(len(arr)):
#         for j in range(i,len(arr)):
#             if(arr[i]+arr[j]==target):
#                 if(i!=j):
#                     return list((i,j))
      
def check(arr,target):
    prevmap={}
    for i in range(len(arr)):
        if target-arr[i] in prevmap:
            return list((i,prevmap[target-arr[i]]))  
        else:
            prevmap[arr[i]]=i
x=check([3,2,4],6)
print(x)