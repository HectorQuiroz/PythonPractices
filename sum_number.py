#Problem Link https://leetcode.com/problems/two-sum/
nums = [3,3]
target = 6
i=0
Output=[]
for num in nums:
    i=i+1
    if i<len(nums):
        x=num+nums[i]
        y=i-1
        if target == x:
            Output.append(y)
            Output.append(i)
    #else:
    #print(Output)
print(Output)
