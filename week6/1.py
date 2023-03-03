import re
x = input()
def text_match(text):
        patterns = '^a(b*)$'
        if re.search(patterns,  text):
                return 'True'
        else:
                return('False')
            
print(text_match(x))