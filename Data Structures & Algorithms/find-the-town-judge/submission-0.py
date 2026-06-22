from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        '''
        Questions:
        1. Town judge exists?? Not always

        BRUTE FORCE
        1. create a hash map for each person (labelled 1 - n)
        2. loop thorugh trust array and assign trust values to respective entities
        3. loop through hash map and check for if hash_map[i].length == 0

        OPTIMIZED
        1. create an adjacency list with person as the key 
        2. create an array with [int (people they trust), int (people who trust in them)]
        '''

        '''
        trusters = { i: set() for i in range(1, n + 1) } # list of who they trust
        trustees = { i: set() for i in range(1, n + 1) } # list of who trusts them

        for truster, trustee in trust:
            trusters[truster].add(trustee)
            trustees[trustee].add(truster)

        for truster in trusters:
            if not len(trusters[truster]) and len(trustees[truster]) == n - 1:
                return truster

        return -1
        '''

        village = { i: [0, 0] for i in range(1, n + 1) }

        for truster, trustee in trust:
            village[truster][0] += 1
            village[trustee][1] += 1

        
        for townsman in village:
            if not village[townsman][0] and village[townsman][1] == n - 1:
                return townsman

        return -1