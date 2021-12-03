import sys

try:

    if len(sys.argv) != 4:
        raise Exception("Invalid syntax!")

    key = str(sys.argv[1])
    f = str(sys.argv[2])
    g = str(sys.argv[3])

    if not (key.isalnum()) or not(9 < len(key) < 16):
        raise Exception("Invalid key!")

    def get(key):
        while True:
            for x in key:
                yield x

    with open(f, "rb") as input:
        with open(g, "wb") as output:

            def xor_operation(data, key) -> bytes:
                return bytes(data ^ key for data, key in zip(data, get(key)))

            output.write(xor_operation(input.read(), str.encode(key)))

except:

    print("Syntax: python3 decrypt.py <key> <input_file> <output_file>")
    exit()