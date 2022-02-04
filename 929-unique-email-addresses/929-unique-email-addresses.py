class Solution:
    def numUniqueEmails(self, emails) -> int:
        sets=set()
        for email in emails:
            d,e=email.split("@")
            d=d.replace('.','')
            d=d.split("+")[0]
            sets.add(d+"@"+e)
        return len(sets)
        