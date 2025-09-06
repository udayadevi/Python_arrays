#used to find the consecutive ones
nums=[1,1,1,0,1,1,0,1,1,1,1]
c=0
maxi=0
for i in range(len(nums)):
    if nums[i]==1:
        c+=1
    else:
        c=0
    maxi=max(maxi,c)
print(maxi)
#time complexity is: o(n)
#space complexity is:o(1)
