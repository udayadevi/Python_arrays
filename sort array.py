#checking if the array is osretd or not 
nums=[1,3,4,2]
for i in range(1,len(nums)):
    if nums[i]<nums[i-1]:
        print("False")
        break
else:
    print("True")