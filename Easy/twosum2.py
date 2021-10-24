def twoSum(numbers, target):
    a,b=0,len(numbers)-1
    while a!=b:
        if(numbers[a]+numbers[b]==target):
            return [a+1,b+1]
        if(numbers[a]+numbers[b]>target):
            b-=1
        else:
            a+=1
            
print(twoSum([1,2,3,4,5,6],8))