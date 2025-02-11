from typing import List
def searchRange(nums: List[int], target: int) -> List[int]:
    # write your code here ^_^
    if not nums:  # If the list is empty
        return [-1, -1]

    noi = []

    for i in range(len(nums)):
        if nums[i] == target:
            noi.append(i)

    if noi:
        return [noi[0], noi[-1]]
    return [-1, -1]
print(searchRange([], 6))
