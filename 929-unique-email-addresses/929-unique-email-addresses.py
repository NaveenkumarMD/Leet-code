class Solution:
    def numUniqueEmails(self, emails) -> int:
        sets=set()
        for email in emails:
            s=""
            d,e=email.split("@")
            d=d.replace('.','')
            if '+' in d:
                d=d[:d.find('+')]
            sets.add(d+"@"+e)
            s=""
        print(sets)
        return len(sets)
        