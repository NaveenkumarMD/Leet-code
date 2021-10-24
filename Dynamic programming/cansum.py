#Given  a target and an array of numbers find whether it is possible to get the sum or not with repetition

# brute force

# def check(target,nums):
#     if target==0:
#         return True
#     if target<0:
#         return False
#     for num in nums:
#         remainder=target-num
#         if(check(remainder,nums)):
#             return True
#     return False

# print(check(900000,[5,4,3,7]))

#memoization

def check(target,nums,dit={}):
    if target==0:
        return True
    if target<0:
        return False
    if target in dit:
        return dit[target]
    for num in nums:
        remainder=target-num
        temp=check(remainder,nums)
        dit[remainder]=num
        if temp:
            return True
    dit[target]=False
    return False

print(check(000,[7,14]))