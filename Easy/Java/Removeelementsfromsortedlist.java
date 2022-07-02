def rightRotate(lists, num):
    output_list = []
    for item in range(len(lists) - num, len(lists)):
        output_list.append(lists[item])
 
    for item in range(0, len(lists) - num):
        output_list.append(lists[item])
 
    return output_list
 
 

n = int(input())
list_1=[]
for i in range(n):
    x=int(input())
    list_1.append(x)
rotatenum=int(input())

 
