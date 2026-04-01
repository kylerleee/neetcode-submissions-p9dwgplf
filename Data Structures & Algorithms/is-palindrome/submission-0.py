class Solution:
    def isPalindrome(self, s: str) -> bool:
        output_string = ''.join([char for char in s if char.isalnum()])
        if output_string.lower() == output_string[::-1].lower():
            return True
        return False