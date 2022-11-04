'''
Given an array of strings words and an integer k, return the k most frequent
strings.

Return the answer sorted by the frequency from highest to lowest.
Sort the words with the same frequency by their lexicographical order.
'''
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        words_dictionary = {}
        
        # Track each word and its frequency in a dictionary, time complexity O(n)
        for word in words:
            if word in words_dictionary.keys():
                words_dictionary[word] += 1
            else:
                words_dictionary[word] = 1
        print('#'*20)
        print(words_dictionary)

        # Order the dictionary based on the frequency of the keys, return the
        # top k keys in the dictionary, ordered first by frequency and then by
        # alphabetical order
        return sorted(words_dictionary.keys(), key=lambda x: (-words_dictionary[x], x))[:k]


def main():

    lst1 = ["i","love","leetcode","i","love","coding"]
    lst2 = ["the","day","is","sunny","the","the","the","sunny","is","is"]

    solution = Solution()
    print(solution.topKFrequent(lst1, 2))
    print(solution.topKFrequent(lst2, 4))

if __name__ == '__main__':
    main()