from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        def check(i):
            if i%3==0 and i%5==0:
                return "FizzBuzz"
            if i%5==0:
                return "Buzz"
            if i%3==0:
                return "Fizz"
            return str(i)  
        arr=[check(i) for i in range(1,n+1)]
         


        return arr
        
x=Solution()
y=x.fizzBuzz(15)
print(y)