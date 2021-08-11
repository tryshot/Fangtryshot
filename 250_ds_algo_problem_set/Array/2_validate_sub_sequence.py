# Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.
# main_array = [3, -2, 20, 25, 8, -1, 10]
# sequence = [3, 20, 8, -1]
# O(n) time | O(1) space - where n is the length of the array


def validate_subsequence(main_array, seq):
    check = 0
    for elem in main_array:
        if seq[check] == elem:
            check += 1
            if check == len(seq):
                break
    return check == len(seq)
            

response =validate_subsequence([3, -2, 20, 25, 8, -1, 10], [3, 20, 8, -1])
print(response)

