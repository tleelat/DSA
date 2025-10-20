#string palindrome using recursion
# Constraints : 1 ≤ s.size() ≤ 106
#The string s contains only lowercase english letters (a-z).



class Solution:
    # helper that checks s[left .. right]
    def solve(self, s, left, right):
        if left >= right:        # crossed over → all pairs matched
            return True
        if s[left] != s[right]:  # mismatch
            return False
        # move both pointers inward
        return self.solve(s, left + 1, right - 1)

    def isPalindrome(self, s: str) -> bool:
        # check the whole string
        return self.solve(s, 0, len(s) - 1)