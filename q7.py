def encrypt(text, keyword):
    result = []
    keyword = keyword.lower()
    k_len = len(keyword)
    for i, char in enumerate(text.lower()):
        p_val = ord(char) - ord('a')
        k_val = ord(keyword[i % k_len]) - ord('a')
        c_val = (p_val + k_val) % 26
        result.append(chr(c_val + ord('a')))
    return ''.join(result)

def decrypt(cipher, keyword):
    result = []
    keyword = keyword.lower()
    k_len = len(keyword)
    for i, char in enumerate(cipher.lower()):
        c_val = ord(char) - ord('a')
        k_val = ord(keyword[i % k_len]) - ord('a')
        p_val = (c_val - k_val) % 26
        result.append(chr(p_val + ord('a')))
    return ''.join(result)

# Given input from practical question
plain_text = "she is listening"
keyword = "pascal"

# Ignore spaces
clean_text = plain_text.replace(" ", "")

cipher_text = encrypt(clean_text, keyword)
decrypted_text = decrypt(cipher_text, keyword)

print("--- Vigenere Cipher ---")
print("Plain Text :", plain_text)
print("Clean Text :", clean_text)
print("Keyword    :", keyword)
print("Encrypted  :", cipher_text)
print("Decrypted  :", decrypted_text)
