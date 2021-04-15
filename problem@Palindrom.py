def checkPalindrom(var):
    s = str(var).lower()
    i = 0
    j = len(s)-1
    while i<j:
        if s[i]!=s[j]:
            print("This is not palindrom")
            return
        i += 1
        j -= 1
    print("This is palindrom")
    

s = 'Asa'
checkPalindrom(s)