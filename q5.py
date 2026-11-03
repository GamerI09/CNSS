def encrypt(key, text):
    cipher_text = ""
    prev_ord = -1
    for letter in text:
        if letter.isalpha():
            if prev_ord == -1:
                cipher_text += chr((((ord(letter) - ord('a')) + key) % 26) + ord('a'))
                prev_ord = (ord(letter) - ord('a'))
            else:
                cipher_text += chr((((ord(letter) - ord('a')) + prev_ord) % 26) + ord('a'))
                prev_ord = (ord(letter) - ord('a'))
        else:
            cipher_text += letter
    return cipher_text

def decrypt(key, text):
    plain_text = ""
    prev_ord = -1
    for letter in text:
        if letter.isalpha():
            if prev_ord == -1:
                plain_text += chr((((ord(letter) - ord('a')) - key) % 26) + ord('a'))
                prev_ord = (((ord(letter) - ord('a')) - key) % 26)
            else:
                plain_text += chr((((ord(letter) - ord('a')) - prev_ord) % 26) + ord('a'))
                prev_ord = (((ord(letter) - ord('a')) - prev_ord) % 26)
        else:
            plain_text += letter
    return plain_text

text = "followwolf"
key = 15
cipher_text = encrypt(key, text)
print("Original Text:", text)
print("Encrypted Text:", cipher_text)
print("Decrypted Text:", decrypt(key, cipher_text))
