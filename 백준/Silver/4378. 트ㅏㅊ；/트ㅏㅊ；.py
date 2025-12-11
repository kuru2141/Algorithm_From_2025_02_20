keys = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"

while True:
    try:
        tmp = input()
        result = ""

        for e in tmp:
            if e == ' ':
                result += ' '
            else:
                idx = keys.find(e)
                result += keys[idx - 1]

        print(result)
    except:
        break