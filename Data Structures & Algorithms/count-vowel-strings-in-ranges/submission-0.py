class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        '''
        Questions 
        1. words cannot be empty 
        2. words[i] cannot be empty
        '''
        # O(m * n) + O(q)
        # that start and end with a vowel?
        prefix = [0 for _ in range(len(words) + 1)]
        vowels = set(["a","e","i","o","u"])
        res = []

        def is_valid(word):
            start = word[0]
            end = word[-1]

            return start in vowels and end in vowels

        for index in range(len(words)):
            word = words[index]
            if is_valid(word):
                prefix[index + 1] = prefix[index] + 1
            else:
                prefix[index + 1] = prefix[index]

        for end, start in queries:
            res.append(prefix[start + 1] - prefix[end])

        return res

