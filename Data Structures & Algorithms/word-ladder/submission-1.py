from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # default case 
        if endWord not in wordList:
            return 0

        adjList = defaultdict(list)

        # i guess regarding the visited set, we can't really be bothered if begin word appears in the list twice 
        wordList.append(beginWord) # add begin word to word list

        '''
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                adjList[pattern].append(word)
        '''
        for i in range(len(wordList)):
            for j in range(len(wordList[i])):
                pattern = wordList[i][:j] + "*" + wordList[i][j + 1:]
                for k in range(len(wordList)):
                    # if same word, skip
                    if i == k:
                        continue
                
                    if pattern == wordList[k][:j] + "*" + wordList[k][j + 1:]:
                        adjList[wordList[i]].append(wordList[k])

        queue = deque([beginWord])
        visited = set([beginWord])
        res = 1 # starting with 1 because we count the "nodes" needed to convert to endWord
    
        while queue:
            # get the children
            for _ in range(len(queue)):
                word = queue.popleft()

                if word == endWord:
                    return res

                for node in adjList[word]:
                    if node not in visited:
                        queue.append(node)
                        visited.add(node)

            res += 1

        return 0
                