def decode(string):
    if not string:
        return("")
    repeats = ''
    code = ''
    for c in string:
        if c.isnumeric():
            repeats += c
        else:
            code += c * (int(repeats) if not repeats == '' else 1)
            repeats = ''
    return code

def encode(string):
    if not string:
        return("")
    code = ""
    rl = 0
    i = 0
    while i < len(string):
        current = string[i]
        rl = 1
        j = i+1
        while j < len(string) and string[j] == current:
            j += 1
            rl += 1
        i = j
        code += f"{str(rl)}{current}" if rl != 1 else f"{current}"
    return code
    
if __name__ == "__main__":
    print(decode('23A3B4C'))
    print(encode("XXXYZZ"))
