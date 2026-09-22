class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj_list = defaultdict(list)
        visited = {beginWord}
        queue = deque([beginWord])
        count = 1

        # construct word dictionary
        for word in wordList:
            for i in range(len(word)):
                substring = word[:i] + "*" + word[i+1:]
                adj_list[substring].append(word)

        # start deque
        while queue:
            length = len(queue)

            for i in range(length):
                top = queue.popleft()

                if top == endWord:
                    return count 

                # add all wild cards into queue
                for i in range(len(top)):
                    substring = top[:i] + "*" + top[i+1:]

                    for word in adj_list[substring]:
                        if word not in visited:
                            visited.add(top)
                            queue.append(word)
            
            count += 1

        return 0