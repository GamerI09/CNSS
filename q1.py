def encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('a')
            result += chr((ord(char) - base + key) % 26 + base)
    return result

def decrypt(cipher, key):
    result = ""
    for char in cipher:
        if char.isalpha():
            base = ord('a')
            result += chr((ord(char) - base - key) % 26 + base)
    return result

plain_text = "this message is easy to encrypt but hard to find the key"
key = 15

clean_text = plain_text.replace(" ", "")

cipher_text = encrypt(clean_text, key)
decrypted_text = decrypt(cipher_text, key)

print("Original Text :", plain_text)
print("Clean Text    :", clean_text)
print("Key           :", key)
print("Encrypted     :", cipher_text)
print("Decrypted     :", decrypted_text)
