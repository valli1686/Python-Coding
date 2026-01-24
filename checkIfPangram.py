class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sentence = set(sentence)
        for x in 'abcdefghijklmnopqrstuvwxyz':
            if x not in sentence:
                return False

        return True