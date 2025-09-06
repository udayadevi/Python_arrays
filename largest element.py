# To find the largest eleemnt here
#Brute force approach
nums=[1,2,3,8,4,9]
nums.sort()
print(nums[-1])
#Time compolexity o(n log n)
#Space complexity o(n)
#Optimized approach
a=[1,8,3,4,7,5,6]
max=a[0]
for i in range(len(a)):
    if a[i]>max:
        max=a[i]
print(max)
#Time complexity is o(n)
#space complexity is o(1)


