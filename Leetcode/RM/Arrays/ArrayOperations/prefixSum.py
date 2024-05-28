
nums = [10, 30, 50, 60, 70, 90]

prefix = [nums[0]]

for i in range(1, len(nums)):
    prefix.append(prefix[-1] + nums[i])

print(prefix)