from enum import verify


def linear_search(list,target):
    
    
    for i in range(0,len(list)) :
        if list[i] == target:
          return i
    return None


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
result = linear_search(numbers, 17)
verify(result)
