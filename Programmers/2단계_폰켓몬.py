def solution(nums):
    k = set(nums)
    return min(len(k),len(nums)/2)