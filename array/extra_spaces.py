
# Remove extra spaces from a string

# Given a string containing many consecutive spaces, trim all spaces so that all words should contain only a single space between them. The conversion should be done in-place and solution should handle trailing and leading spaces and also remove preceding spaces before common punctuation like full stop, comma and a question mark.
# https://www.geeksforgeeks.org/remove-extra-spaces-string/
# Examples: 

# Input: 
# str = "   Hello Geeks . Welcome   to  GeeksforGeeks   .    ";
# Output: 
# "Hello Geeks. Welcome to GeeksforGeeks."
# Input: 
# str = "GeeksforGeeks";
# Output: 
# "GeeksforGeeks"


#current = " "
#next = " "


def extra_spaces(str):
    cur_i = 0
    next_i = 1
    had_period = False
    init = True
    answer = ''
    while len(str) > next_i:
        should_keep = (had_period or str[next_i].isalpha()) and (not init)
        if (str[cur_i] != " " or should_keep):
            answer += str[cur_i]
            init = False
        if (str[cur_i] == '.'):
            had_period = True
        else:
            had_period = False
        cur_i += 1
        next_i += 1
    if str[-1] != " ":
        answer += answer + str[-1]
    return answer

# should be: "Hello Geeks. Welcome to GeeksforGeeks."
print(extra_spaces("   Hello Geeks . Welcome   to  GeeksforGeeks   .    "))