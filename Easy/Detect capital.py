class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        import re
        regex = re.compile(r'[A-Z]([a-z]*|[A-Z]*)$|[a-z]*$')
        if regex.match(word):
            return True
        return False