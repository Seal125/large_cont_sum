'''
PEDAC Process

P - Given a list of positive and negative numbers, find the  sum that is the largest given a consecutive sequence

E - print(large_cont_sum([1,2,-1,3,4,10,10,-10,-1]) == 29)
    print(large_cont_sum([1,2,-1,3,4,-1]) == 9)
    print(large_cont_sum([-1,1]) == 1)
    print(large_cont_sum([2,4,5,-3,6,8]) == 22)
    print(large_cont_sum([1,2,-2,-3,4,5,10]) == 19)

D - Lists

A - 1. Create two variables, one called `current_sum` and one called `max_sum`
        a. Initialize `current_sum` with the first element on the list
    2. Loop through the list
        a. If the current_sum is less than the current_sum plus the next number, add that number
        b. If the current_sum is larger than the max_sum, assign current_sum to max_sum
    3. Return max_sum
'''

def large_cont_sum(lst):
    current_sum = lst[0]
    max_sum = lst[0]

    if len(lst) == 2:
        if sum(lst) > max(lst):
            max_sum = sum(lst)
            return max_sum
        else:
            max_sum = max(lst)
            return max_sum

    for num in lst[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(current_sum, max_sum)

    return max_sum

print(large_cont_sum([1,2,-1,3,4,10,10,-10,-1]) == 29)
print(large_cont_sum([1,2,-1,3,4,-1]) == 9)
print(large_cont_sum([-1,1]) == 1)