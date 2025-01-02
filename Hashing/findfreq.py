"""
You're given an array (arr)
Return the frequency of element x in the given array

https://www.geeksforgeeks.org/problems/find-the-frequency/1 

"""

class Solution:
    def findFrequency(self, arr, x):
        # code here
        
        hash_map = dict() 
        n = len(arr)
        for i in range(0,n): 
            hash_map[arr[i]] = hash_map.get(arr[i],0) + 1 
        
        return hash_map.get(x,0)
    