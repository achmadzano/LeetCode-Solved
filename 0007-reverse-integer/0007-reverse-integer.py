class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Check if the integer is negative
        is_negative = x < 0
        
        # Convert the absolute value of x to a string, reverse it, and convert back to integer
        reversed_str = str(abs(x))[::-1]
        reversed_int = int(reversed_str)
        
        # If the original integer was negative, make the reversed integer negative as well
        if is_negative:
            reversed_int = -reversed_int
        
        # Check for integer overflow
        if reversed_int < INT_MIN or reversed_int > INT_MAX:
            return 0
        
        return reversed_int
