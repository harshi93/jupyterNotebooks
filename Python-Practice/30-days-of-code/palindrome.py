def isPalindrome(string):
    first_index = 0
    last_index = len(string) - 1
    middle_index = int((first_index + last_index) / 2)
    string2 = ""
    string3 = ""
    isPalindrome = False

    for i in range(0, middle_index):
        string2 += string[i]

    for j in range(last_index, middle_index, -1):
        string3 += string[j]

    if (string2 == string3):
        isPalindrome = True
        return bool(isPalindrome)

    if (string2 != string3):
        return bool(isPalindrome)

