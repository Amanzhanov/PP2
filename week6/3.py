import re
x = input()
def text_match(text):
        patterns = '^[a-z]+_[a-z]+$'
        if re.search(patterns,  text):
                return 'True'
        else:
                return('False')
print(text_match(x))