import math
if __name__=="__main__":
    def check(value):
        low=0
        high=value
        ans=-1
        while(low<=high):
            mid=math.floor((low+high)/2)
            res=mid*mid
            if res==value:
                return mid
            elif res<value:
                low=mid
                ans=mid
            else:
                high=mid
        return ans
                    
    print(check(int(input())))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # def check(value):
    #     i=0
    #     j=value
    #     def dfs(i,j):
    #         mid=((i+j)/2)
    #         res=mid**2
    #         if value==res:
    #             return mid
    #         elif res<value:
    #             dfs(mid+1,j)
    #         else:
    #             dfs(i,mid-1)
    #     return dfs(i,j)
        
    # print(check(16))
                
                