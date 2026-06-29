from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        # Using defaultdict automatically initializes an empty list [] for any new key
        anagram_map = defaultdict(list)
        
        for s in strs:
            # 1. Sort the characters of the string alphabetically
            # sorted("cat") returns ['a', 'c', 't']
            # "".join() turns it back into a string: "act"
            sorted_key = "".join(sorted(s))
            
            # 2. Append the original string to its matching sorted key group
            anagram_map[sorted_key].append(s)
            
        # 3. Return only the groups of anagrams
        return list(anagram_map.values())