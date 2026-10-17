import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        droppedPunctuation = s.maketrans("","", string.punctuation)
        sanitizedString = s.translate(droppedPunctuation).replace(" ", "").lower()

        i = 0
        j = len(sanitizedString) - 1

        while i <= j:
            if sanitizedString[i] != sanitizedString[j]:
                return False
            i = i + 1
            j = j - 1
        return True


# strip spacing
# strip  any symbol/punctuation
# capital
# first pointer at start, second pointer at end, meet at middle