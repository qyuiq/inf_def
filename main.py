#шифр цезаря
def zad_1():
    alphabet = ["а", "б", "в", "г", "д", "е", "ж", "з", "и", "к", "л", "м", 'н', "о", "п",
                "р", "с", "т","у", "ф", "х", "ц", "ч", "ш", "щ", "ь", "ы", "ъ", "э", "ю", "я"]
    text = "ЦФЯЬИЮЯЧЫЯЦЬБЯФТЮЬЧУЗЫФ".lower()

    for i in range(len(alphabet)):
        k = ""
        for j in text:
            k += alphabet[alphabet.index(j) - i]
        print(k)


#шифр Плейфера
def zad_2():

    def find_index(char):
        for i in range(len(alphabet)):
            try:
                j = alphabet[i].index(char)
                return [i, j]
            except ValueError:
                continue


    def col_row():
        return [alphabet[a][d], alphabet[c][b]]

    def col():
        return [alphabet[a - 1][b], alphabet[c - 1][d]]

    def row():
        return [alphabet[a][b - 1], alphabet[c][d - 1]]

    alphabet = [["р", "е", "с", "п", "у", "б"],
                ["л", "и", "к", "а", "в", "г"],
                ["д", "ж", "з", "м", "н", "о"],
                ["т", "ф", "х", "ц", "ч", "ш"],
                ["щ", "ь", "ы", "э", "ю", "я"]]
    text = "МВЖРЗОЗБФЩЖПШДМЛФГТЕНГМВГЬ".lower()
    decode = ""
    while not len(text) == 0:
        buf = text[0:2]
        symb1, symb2 = "", ""
        a, b = find_index(buf[0])
        c, d = find_index(buf[1])
        if not a == c and not b == d:
            symb1, symb2 = col_row()
        elif b == d:
            symb1, symb2 = col()
        elif a == c:
            symb1, symb2 = row()
        decode += symb1 + symb2
        text = text[2:]

    print(decode)


#шифр перестановкой только внутри блока данных
def zad_3():
    key = '365142'
    text = "иицпнрвузпи_ьгоанлпгоор_мрирмааяионв"
    blocks = [text[i:i+len(key)] for i in range(0, len(text), len(key))]
    decode = ""
    for block in blocks:
        for i in range(len(block)):
            decode += block[key.index(str(i+1))]
    print(decode)



zad_1()