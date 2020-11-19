znaki = input("Podaj znaki -> ")

def substring(string, an, index, is_char):
    if index == len(string)-1:
        if is_char:
            print(an)
            print(an+string[index])
        else:
            if ord(string[index]) >= ord("a") and ord(string[index]) <= ord("z"):
                print(an+string[index])

    else:
        substring(string, an, index + 1, is_char)
        is_char = is_char or (ord(string[index]) >= ord("a") and ord(string[index]) <= ord("z"))
        substring(string, an + string[index], index + 1, is_char)


substring(znaki, "", 0, False)