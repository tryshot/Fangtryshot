# Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.
# main_array = [3, -2, 20, 25, 8, -1, 10]
# sequence = [3, 20, 8, -1]
# O(n) time | O(1) space - where n is the length of the array

def validate_subsequence(array, sequence):
    result = False
    check = 0 
    # import pdb; pdb.set_trace()
    for elem in array:
        if sequence[check] == elem:
            check = check + 1
            if check == len(sequence):
                result = True
                break
    return result



response =validate_subsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6,-1, 10])
print (response)