class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = set()

        words.sort(key=lambda x: len(x))

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                print(words[i], words[j])
                if words[i] in words[j]:
                    res.add(words[i])
        
        return list(res)
