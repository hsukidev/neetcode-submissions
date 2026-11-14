class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # get the greater length of the 2
        # iterate that many times over both words
        # if word1 either word is shorter, just end that word and append the rest
        max_length = max(len(word1), len(word2))
        new_word = ''
        for i in range(0, max_length):
            if i < len(word1):
                new_word += word1[i]
            if i < len(word2):
                new_word += word2[i]

        return new_word