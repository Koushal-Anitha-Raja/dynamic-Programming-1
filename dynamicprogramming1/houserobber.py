#TC: O(n)
#SC: O(n)

class Solution:
    def rob(self, nums: List[int]) -> int:
        """if len(nums)==1:
            return nums[0]
        
        #using two variables
        var1=nums[0]
        var2=max(nums[0],nums[1])
    
        for i in range(2,len(nums)):
            var2 = (max(nums[i] + var1, var2))
        return var2"""
        
        #declaring a dp array 
        dp=[]
        
        #if the input array has only one element
        if len(nums)==1:
            return nums[0]
        #just append it directly to the dp array
        dp.append(nums[0])
        
        #if the input array has two variable then check the max between them
        dp.append(max(nums[0],nums[1]))
    
    
        #iterate the input array nums except first two elements as we checked the conditions before itself
        for i in range (2,len(nums)):
            #the logic to carry the largest robbed value by using nums array and dp array
            dp.append(max(nums[i]+dp[i-2],dp[i-1]))
            
        #returning the last element in dp array as it will carry the largest robbed value    
        return dp[-1]    
            
            
