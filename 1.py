nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
temp = nums[3:]
temp.sort()
print (nums)
print(temp)
current = 3
for i in range(len(temp)):
    nums[current] = temp[i]
    current += 1
print(nums)

