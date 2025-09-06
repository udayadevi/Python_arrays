#checking if the array is osretd or not 
nums=[1,3,4,2]
for i in range(1,len(nums)):
    if nums[i]<nums[i-1]:
        print("False")
        break
else:
    print("True")
#Time complexity is o(n)
#Space complexity is o(1)




#like for another condition
a=[1,2,3,4]
for i in range(1,len(nums)):
    if a[i]<a[i-1]:
        print("False")
        break
else:
    print("True")
