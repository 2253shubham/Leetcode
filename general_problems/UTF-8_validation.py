# Problem description here https://leetcode.com/problems/utf-8-validation/description/

from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def num_bytes(intg):
            """Determine the number of bytes in a UTF-8 character."""
            if intg & 0b10000000 == 0:  # 1-byte (0xxxxxxx)
                return 1
            elif intg & 0b11100000 == 0b11000000:  # 2-byte (110xxxxx)
                return 2
            elif intg & 0b11110000 == 0b11100000:  # 3-byte (1110xxxx)
                return 3
            elif intg & 0b11111000 == 0b11110000:  # 4-byte (11110xxx)
                return 4
            else:
                return -1  # Invalid leading byte

        i = 0
        while i < len(data):
            num_bytes_needed = num_bytes(data[i])
            if num_bytes_needed == -1 or num_bytes_needed > len(data) - i:
                return False
            
            # Check continuation bytes
            for j in range(1, num_bytes_needed):
                if data[i + j] & 0b11000000 != 0b10000000:  # Not 10xxxxxx
                    return False
            
            i += num_bytes_needed  # Move to next character
        
        return True

# Time Complexity = O(N), Space Complexity = O(1) 


"""
# My original implementation (Worse time complexity of O(NlogN))
# Extra logN introduced by using the bin operation

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def utf_byte_check(intg):
            biny = bin(intg)[2:].zfill(8)
            if biny[0:4] == "1111" and biny[4] == "0":
                return 4
            elif biny[0:3] == "111" and biny[3] == "0":
                return 3
            elif biny[0:2] == "11" and biny[2] == "0":
                return 2
            elif biny[0] == "0":
                return 1
            else:
                return -1


        def utf_sub_byte_check(intg):
            biny = bin(intg)[2:].zfill(8)
            if biny[0] == "1" and biny[1] == "0":
                return True
            else:
                return False


        def utf_folw_byte_check(sub_data):
            for i in range(len(sub_data)):
                if utf_sub_byte_check(sub_data[i]) == False:
                    return False

            return True 

        i = 0
        while i < len(data):
            ln = utf_byte_check(data[i])
            if ln > len(data) - i:
                return False
            if ln > 1:
                check = utf_folw_byte_check(data[i+1: i+ln])
            elif ln == -1:
                check = False
            else:
                check = True
            
            if check == False:
                return False
            
            i += ln
        
        return True
"""
                
            
        