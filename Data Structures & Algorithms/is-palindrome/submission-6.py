class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s) - 1
        l = 0
        while l<n:
            while l<n and not s[l].isalnum():
                l+=1
            while l<n and not s[n].isalnum():
                n+=-1
            if s[l].lower() != s[n].lower():
                return False
            n+=-1
            l+=1
        return True
        