nums=[int(x) for x in open("input1.txt").readlines()]

def ex1(nums):
  ans=0
  last=nums[0]
  for x in nums:
    if x>last:
      ans+=1
    last=x
  print(ans)
ex1(nums)
nums2=[]
for i in range(len(nums)-2):
  nums2.append(nums[i]+nums[i+1]+nums[i+2])  
ex1(nums2)