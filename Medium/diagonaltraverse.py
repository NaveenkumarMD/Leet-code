def traverse(mat):
    dit={}
    for r in range(len(mat)):
        for c in range(len(mat[0])):
            if r+c in dit:
                dit[r+c].append(mat[r][c])
            else:
                dit[r+c]=[mat[r][c]]
    print(dit)
    arr=[]
    for i in range(len(mat)+len(mat[0])-1):
        if i%2==1:
            arr.extend(dit[i])
        else:
            arr.extend((dit[i][::-1]))
    print( arr)
            
        
    
    
if __name__ == '__main__':
    traverse(mat = [[1,2,3],[4,5,6],[7,8,9]])
    