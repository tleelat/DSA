
## https://www.geeksforgeeks.org/problems/frequency-of-array-elements-1587115620/0 

class Solution:
    def frequencyCount(self, arr):
        #  code here
        hash_map = dict() 
        n = len(arr) 
        for i in range(n): 
            hash_map[arr[i]] = hash_map.get(arr[i],0) + 1 
                    
        result = []
        for x in range(1,n+1): 
            result.append(hash_map.get(x,0))
            
        return result