from typing import List
def removeDuplicates(nums: List[int]) -> int:
    # write your code here ^_^
    count={}
    nl=[]
    for num in nums:
        count[num] = count.get(num, 0) + 1
        if count[num] <= 2:  # Allow at most 2 occurrences
            nl.append(num)  # Append the valid element to new_list
    return len(nl)

print(removeDuplicates([1, 1, 1, 2, 2, 3]))
