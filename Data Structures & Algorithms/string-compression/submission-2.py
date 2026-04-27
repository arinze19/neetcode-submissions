class Solution:
    def compress(self, chars: List[str]) -> int:
        # if len(chars) == 1: return chars
        # i = 0; j = 0
        # while i < len(chars):
        # while j < len(chars) and chars[i] == chars[j]:
        #   j += 1  
        # count = j - i
        # for item in stringified count:
        #   chars[i + 1 + k] = item
        # i = j
        #   
        i = 0
        j = 0 
        k = 0
        n = len(chars)

        while i < n:
            chars[k] = chars[i]
            k += 1
            while j < n and chars[i] == chars[j]:
                j += 1
            count = j - i

            if count > 1:
                for char in str(count):
                    chars[k] = char
                    k += 1
            i = j

        # How to get the length of the compressed string
        # j - 1??
        # end + 1??

        return k


        # while 