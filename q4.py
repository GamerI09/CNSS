def encrypt(k1, k2, text):
    cipher_text = ""
    for letter in text:
        if letter.isalpha():
            cipher_text += chr((((ord(letter) - ord('a')) * k1 + k2) % 26) + ord('a'))
        else:
            cipher_text += letter
    return cipher_text

def decrypt(k1, k2, text):
    plain_text = ""
    k1_inv = pow(k1, -1, 26)
    for letter in text:
        if letter.isalpha():
            plain_text += chr(((((ord(letter) - ord('a')) - k2) * k1_inv) % 26) + ord('a'))
        else:
            plain_text += letter
    return plain_text

text = "hello"
k1 = 7
k2 = 2
cipher_text = encrypt(k1, k2, text)
print("Original Text:", text)
print("Encrypted Text:", cipher_text)
print("Decrypted Text:", decrypt(k1, k2, cipher_text))
