from heapq import heapify, heappop,heappush
li=[]
for i in [23,4,3,1,2,3,4,23,455,90]:
    heappush(li,-1*i)
heapify(li)
print(li)
while li:
    print(heappop(li)*-1)