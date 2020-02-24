"""
Given a string S of length N that is indexed from 0 to N-1, print it's even indexed characters
and odd indexed characters as 2 space separated strings on a line
"""

string = "Harshit"

even_index_char_string = ""
odd_index_char_string = ""

for i in range(0,len(string)):
    if(i%2 == 0):
        even_index_char_string = even_index_char_string + string[i]
    else:
        odd_index_char_string = odd_index_char_string + string[i]

print(even_index_char_string + "  " + odd_index_char_string)