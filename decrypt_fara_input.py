import sys

f = sys.argv[1]

with open(f, "rb") as input:

    file = input.read()

    sol_list = []

    def printable_char(x):
        return 48 <= ord(x) <= 57 or 65 <= ord(x) <= 122

    def get_max(char_dict):
        return max(char_dict, key= char_dict.get)

    def guess(most_fr_char):
        if printable_char(chr(most_fr_char ^ 32)):
            return chr(most_fr_char ^ 32)
        elif printable_char(chr(most_fr_char ^ 97)):
            return chr(most_fr_char ^ 97)
        elif printable_char(chr(most_fr_char ^ 105)):
            return chr(most_fr_char ^ 105)
        elif printable_char(chr(most_fr_char ^ 101)):
            return chr(most_fr_char ^ 101)

    for key_len in range(10, 16):

        sol = ''

        poz = 0
        freq_list = [{} for x in range(0,key_len)]

        for x in file:
            freq_list[poz][x] = 1 if x not in freq_list[poz] else freq_list[poz][x] + 1
            poz += 1
            poz %= key_len

        for i in range(0, key_len):
            most_fr_char = get_max(freq_list[i])
            sol += guess(most_fr_char)

        sol_list += [sol]

    def dexor(file, key):

        cnt = 0
        size = len(file)
        length = len(key)
        index = 0

        for x in file:
            if printable_char(chr(x ^ ord(key[index]))):
                cnt += 1
            index += 1
            index %= length

        return cnt / size

    mx = 0.50
    final_sol = ''

    for x in sol_list:
        perc = dexor(file, x)
        if perc > mx:
            mx = perc; final_sol = x

    print(final_sol)
