'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced 
to get t.

All occurrences of a character must be replaced with another character while 
preserving the order of characters. No two characters may map to the same 
character, but a character may map to itself.
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
    
        # Dictionaries to map each char to another
        map_s_t = {}
        map_t_s = {}

        # The two strings have the same length per problems description
        for ch1, ch2 in zip(s, t):
            # If the two keys are not in the dictionaries
            if ch1 not in map_s_t and ch2 not in map_t_s:
                map_s_t[ch1] = ch2
                map_t_s[ch2] = ch1
            # If the keys are in the dictionaries, the values have to correspond
            # or else the two strings are not isomorphic
            elif map_s_t.get(ch1) != ch2 or map_t_s.get(ch2) != ch1:
                return False

        return True