function that takes in a non-empty array of distinct integers and second param is
a target sum. If any two numbers in the input array sum
up to the target sum, the function should return them in an array, or else return
an empty array.
Note : target sum with 2 distinct Integers only


[-1, 2, 3, 5, 7, 8, 11]  = 14    


#1) O(n^2) time | O(1) space
def twoNumberSum(array, target_sum):
    for x in array:
        for y in array:
            if x == y:
                continue
            if x+y ==target_sum:
                return [x, y]
    return []

#2) O(n) time | O(n) space
def twoNumberSum(array, target_sum):
    check = {}
    for x in array:
        find_number = target_sum -x
        if find_number in check.keys():
            return [x, find_number]
        else:
            check[x] = True
    return []
    
    
#3) O(n Log(n)) time | O(1) space
def twoNumberSum(array, target_sum):
    array.sort()
    print (array)
    left, right = 0, len(array) -1
    while left < right:
        cur_sum = array[left] + array[right]
        if cur_sum == target_sum:
            return [array[left], array[right]]
        elif cur_sum < target_sum:
            left += 1
        elif cur_sum > target_sum:
            right -= 1
    return []
    
response = twoNumberSum([-1, 3, 2, 5, 8, 7, 11], 14)
print (response)