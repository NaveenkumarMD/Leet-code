

# get user input in a array
def get_input():
    user_input = input("Enter numbers separated by a comma:\n").strip()
    return [int(item) for item in user_input.split(',')]

# bubble sort
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def average(array):
    return sum(array)/len(array)
arr=get_input()
print(bubble_sort(arr))
print(average(arr))