class Solution:
    def lemonadeChange(self, bills) -> bool:
        dit={
            20:0,10:0,5:0
        }
        for i in bills:
            if i==5:
                dit[5]+=1
            elif i==10:
                if dit[5]==0:
                    return False
                else:
                    dit[5]-=1
                    dit[10]+=1
            else:
                if dit[10]==0 and dit[5]>=3:
                    dit[5]-=3
                    dit[20]+=1
                elif dit[10]>=1 and dit[5]>=1:
                    dit[5]-=1
                    dit[10]-=1
                    dit[20]+=1
                else:
                    return False
        return True
                    
                
x=Solution()
y=x.lemonadeChange([5,5,5,10,20])
print(y)