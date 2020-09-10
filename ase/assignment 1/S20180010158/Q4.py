# Question 4
class LetterFilter:

    def __init__(self, s):
        self.s = s

    def filter_vowels(self):
        # Enter your code here
        string = self.s
        for vowel in 'aeiou':
            string = string.replace(vowel, "")
        return string

    def filter_consonants(self):
        # Enter your code here
        string = self.s
        for consonant in 'bcdfghjklmnpqrstvwxyz':
            string = string.replace(consonant, "")
        return string


def main(s):
    string = LetterFilter(s)
    print(string.filter_vowels())
    print(string.filter_consonants())
