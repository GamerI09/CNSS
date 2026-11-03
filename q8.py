
def inverse(k):
    det = (k[0][0]*k[1][1] - k[0][1]*k[1][0]) % 26
    d = pow(det, -1, 26)

    return [
        [(k[1][1]*d) % 26, (-k[0][1]*d) % 26],
        [(-k[1][0]*d) % 26, (k[0][0]*d) % 26]
    ]


def encrypt(text, key):
    text = text.lower().replace(" ", "")

    if len(text) % 2 != 0:
        text += 'x'

    result = ""

    for i in range(0, len(text), 2):
        p1 = ord(text[i]) - 97
        p2 = ord(text[i+1]) - 97

        c1 = (key[0][0]*p1 + key[0][1]*p2) % 26
        c2 = (key[1][0]*p1 + key[1][1]*p2) % 26

        result += chr(c1+97) + chr(c2+97)

    return result


def decrypt(text, key):
    k = inverse(key)
    result = ""

    for i in range(0, len(text), 2):
        c1 = ord(text[i]) - 97
        c2 = ord(text[i+1]) - 97

        p1 = (k[0][0]*c1 + k[0][1]*c2) % 26
        p2 = (k[1][0]*c1 + k[1][1]*c2) % 26

        result += chr(p1+97) + chr(p2+97)

    return result


plain = "we live in an insecure world"

key = [
    [3, 2],
    [5, 7]
]

cipher = encrypt(plain, key)

print("Plain Text :", plain)
print("Encrypted  :", cipher)
print("Decrypted  :", decrypt(cipher, key))
