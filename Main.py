def cypher(sentance, offset):
    while offset > 26:
        offset -= 26
    alphabetsoup = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y", "z"]
    realwords = ""
    sentance = sentance.casefold()
    sentance = list(sentance)
    for x in range(len(sentance)):
        if sentance[x - 1] == ' ':
            continue
        else:
            sentance[x - 1] = alphabetsoup[alphabetsoup.index(sentance[x - 1]) + offset]
    for y in range(len(sentance)):
        realwords += sentance[y - 1]
    realwords = list(realwords)
    letter = realwords.pop(0)
    realwords.append(letter)
    str1 = " "
    return (str1.join(realwords))



while True:
    encode = input("Do you want to encode or decode? ")
    if encode == "encode":
        text = input("input sentance: ")
        off = int(input("input offset: "))
        print(cypher(text, off))
    # elif encode == "decode":
    #
    # else:
    #     print("Unrecognised input")
