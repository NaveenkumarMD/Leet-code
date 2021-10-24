from typing import List
def countStudents(students: List[int], sandwiches: List[int]) -> int:
    n=len(students)
    j=0
    i=0
    c=0
    while len(students)>0:        
        if students[i]==sandwiches[j]:
            students.pop(0)
            j+=1
            c=0
        else:
            c+=1
            students.append(students.pop(0))
            if(c>=len(students)):
                return len(students)
    return 0      
x=countStudents(students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1])
print(x)