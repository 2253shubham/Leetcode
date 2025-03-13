# Problem description here https://leetcode.com/problems/fraction-to-recurring-decimal/


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # Handle sign
        sign = "-" if numerator * denominator < 0 else ""
        numerator, denominator = abs(numerator), abs(denominator)

        # Compute integer part
        integer_part = str(numerator // denominator)
        remainder = numerator % denominator
        if remainder == 0:
            return sign + integer_part  # No fractional part

        # Compute fractional part
        ans = sign + integer_part + "."
        remainder_map = {}  # To store positions of remainders
        fraction_part = ""

        while remainder != 0:
            if remainder in remainder_map:
                # Insert parentheses at the repeating start index
                index = remainder_map[remainder]
                fraction_part = (
                    fraction_part[:index] + "(" + fraction_part[index:] + ")"
                )
                return ans + fraction_part

            remainder_map[remainder] = len(fraction_part)
            remainder *= 10
            fraction_part += str(remainder // denominator)
            remainder %= denominator

        return ans + fraction_part


# Time Complexity = O(N), Space Complexity = O(N)
# where N is the value of denominator
