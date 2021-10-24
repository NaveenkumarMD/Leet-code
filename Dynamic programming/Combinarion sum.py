#brute force
# def combinationsum(target,nums):
#     if target == 0:
#         return []
#     if target<0:
#         return None
#     for num in nums:
#         remainder=target-num
#         temp=combinationsum(remainder,nums)
#         if temp is not None:
#             return [*temp,num]
#     return None
# x=combinationsum(300,[7,14])
# print(x)


#memoiszation
def combinationsum(target,nums,memo={}):
    if target in memo:return memo[target]
    if target == 0:
        return []
    if target<0:
        return None
    for num in nums:
        remainder=target-num
        temp=combinationsum(remainder,nums)
        if temp is not None:
            memo[target]=[*temp,num]
            return memo[target]
    memo[target]=None
    return None
x=combinationsum(300,[7,14])
print(x)