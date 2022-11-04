'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower
and upper cases, more than once.
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        
        # Define the vowels
        vowels = "AaEeIiOoUu"

        lst = list(s)
        first, last = 0, len(lst) - 1

        while first < last:
            if lst[first] in vowels and lst[last] in vowels:
                lst[first], lst[last] = lst[last], lst[first]
                first += 1
                last -= 1
            elif lst[first] not in vowels and lst[last] in vowels:
                first += 1
            elif lst[first] in vowels and lst[last] not in vowels:
                last -= 1
            else:
                first += 1
                last -= 1
        
        return "".join(lst)


        
def main():
    s1 = "hello"
    s2 = "leetcode"

    solution = Solution()
    print(solution.reverseVowels(s1))
    print(solution.reverseVowels(s2))

if __name__ == '__main__':
    main()