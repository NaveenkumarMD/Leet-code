def dfs(n,position,open,close,s):
    if close==n:
        print(''.join(s))
        return
    else:
        if close<open:
            s[position]='}'
            dfs(n,position+1,open,close+1,s)
        if open<n:
            s[position]='{'
            dfs(n,position+1,open+1,close,s)
def generate(n):
    dfs(3,0,0,0,[""]*2*n)

generate(3)
