#TC: O(n) 
#SC: O(n)

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        #declaring a hashset for storing the nums value
        Hset=[0] * (max(nums)+1)
        
        #iterating the nums array
        for num in nums:
            Hset[num]+=num
            
        #Folllowing the house robber strucutre
        #declaring the dp array as the size of hashset we created
        dp=[0] *len(Hset)
        
        #initializing the 0 th dp index as zero
        dp[0]=0
        
        #initializing the 1 st index of dp array as 1 st index as 0 th index is zero
        dp[1]=Hset[1]
        
        #iterating the value dp array and store max value
        for i in range (2,len(dp)):
            #logic to find the max value through one single pass
            dp[i]=max((Hset[i]+dp[i-2],dp[i-1]))
            
        #returning the final element in the dp array as it stores the max value    
            
        return dp[-1]    
        
