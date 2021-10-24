def check(s):
    arr=[]
    dit={']':'[','}':'{',')':'('}
    for i in s:
        if i in dit.keys():
            top=arr.pop() if arr else ""
            if top!=dit[i]:
                return False
        else:
            arr.append(i)
    return not arr          
print(check('[]({})'))