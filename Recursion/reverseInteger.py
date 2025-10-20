#Reverse an Integer using Recursion

## Constraints :
    #-231 <= x <= 231 - 1

class Solution:
    def reverse(self, x: int) -> int:
        num = abs(x) 
        lastdigit = 0 
        result = 0 
        isnegative = False 

        if x < 0 : 
            isnegative = True 
        
        while num > 0 : 
            lastdigit = num%10 
            result = result*10 + lastdigit 
            num = num//10 
        
        if result < (-(2**31)) or result > ((2**31) - 1): 
            return 0
        return -result if isnegative else result 