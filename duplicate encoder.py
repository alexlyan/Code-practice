# The goal of this exercise is to convert a string to a new string where each character in the new string is
#  "(" if that character appears only once in the original string, or ")" 
# if that character appears more than once in the original string. Ignore capitalization 
# when determining if a character is a duplicate.

def duplicate_encode(word):
    word = word.lower()
    result = ''
    for x in word:
        if word.count(x) > 1:
            result += '('
        else:
            result += ")"
    return result
duplicate_encode("ee33er")


# solution 2
# best one
# def duplicate_encode(word):
#     return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])