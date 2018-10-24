def decode(codes, encoded):
    dctnry = {}

    for code in range(len(codes)):
        codes[code] = codes[code].split('\t')

    for code in codes:
        dctnry[code[1]] = code[0]

    temp = ''
    decoded = ''
    encoded = encoded.strip()

    for value in encoded:
        if temp in dctnry:
            if dctnry[temp] == '[newline]':
                decoded += '\n'
            else:
                decoded += dctnry[temp]

            temp = value
        else:
            temp += value

    if temp in dctnry:
        if dctnry[temp] == '[newline]':
            decoded += '\n'
        else:
            decoded += dctnry[temp]

    return decoded


print(decode(["a\t100100", 'b\t100101', '[newline]\t111111'], '100100111111100101 '))
print(decode(["a\t01", 'b\t10', '[newline]\t110'], '0110'))
print(decode(["a\t100100", 'b\t100101', '[newline]\t111111', 'c\t110001', 'd\t100000', 'p\t111110', 'q\t000001'], '111110000001100100111111100101110001111110 '))
print(decode(["a\t100100", 'b\t100101', '[newline]\t111111', 'c\t110001', 'd\t100000'], '100100111111100101110001100000 '))
