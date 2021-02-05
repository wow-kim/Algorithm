# Enter your code here. Read input from STDIN. Print output to STDOUT

for _ in range(int(input())):
    left = 0
    right = int(input())-1
    nums = list(map(int, input().split(" ")))
    
    stack = [float("Inf")]
    while left <= right:
        if stack[-1] < max(nums[left], nums[right]):
            print("No")
            break
        
        if nums[left] >= nums[right]:
            stack.append(nums[left])
            left += 1
        else:
            stack.append(nums[right])
            right -= 1
    else:
        print("Yes")
    