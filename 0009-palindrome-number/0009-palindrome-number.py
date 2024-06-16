class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            rev_x = str(x)[::-1]
            if int(rev_x) == x:
                return True
            else:
                False
