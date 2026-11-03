def encrypt(text, shift=3):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
    return result

def decrypt(cipher, shift=3):
    result = ""
    for char in cipher:
        if char.isalpha():
            base = ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
    return result

plain_text = "this message is easy to encrypt but hard to find the key"
shift = 3

clean_text = plain_text.replace(" ", "")

cipher_text = encrypt(clean_text, shift)
decrypted_text = decrypt(cipher_text, shift)

print("Original Text :", plain_text)
print("Clean Text    :", clean_text)
print("Key (Shift)   :", shift)
print("Encrypted     :", cipher_text)
print("Decrypted     :", decrypted_text)
