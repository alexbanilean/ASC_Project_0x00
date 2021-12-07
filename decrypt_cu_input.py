import sys

f = sys.argv[1]
g = sys.argv[2]

with open(f, "r", encoding='utf-8') as input:
    with open(g, "rb") as output:

        init = input.read()
        out = output.read()

        for x in range(15):
            print(chr(ord(init[x]) ^ out[x]), end='')
