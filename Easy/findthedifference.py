# def findTheDifference(self, s, t):
#     s=sorted(s)
#     t=sorted(t)
#     for i in range(len(t)):
#         x=t[:i]+t[i+1:]
#         s1=""
#         s1="".join(x)
#         s="".join(s)
#         print(s,s1)
#         if(s==s1):
#             return t[i]

def findTheDifference(self, s, t):
    s1=0
    s2=0
    for i in s:s1+=ord(i)
    for i in t:s2+=ord(i)
    print(chr(s2-s1))