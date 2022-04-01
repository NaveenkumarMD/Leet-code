class Solution:
    def findComplement(self, num: int) -> int:
        x=bin(num).replace("0b","")
        res=""
        for i in x:
            if i=="0":
                res+="1"
            else:
                res+="0"
        return int(res,2)
        