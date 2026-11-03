def ordE(a):
    return ord(a) - ord('a')

def createMatrix(secret):
    matrix = [[0 for j in range(5)] for i in range(5)]
    added_char = set()
    curr = 0
    alpha = 0
    for i in range(5):
        for j in range(5):
            if curr < len(secret):
                val = ordE(secret[curr])
                matrix[i][j] = val
                if val == ordE("i") or val == ordE("j"):
                    added_char.add(ordE("i"))
                    added_char.add(ordE("j"))
                else:
                    added_char.add(val)
                curr += 1
            else:
                while alpha in added_char:
                    alpha += 1
                if alpha == ordE('i') or alpha == ordE('j'):
                    matrix[i][j] = ordE('i')
                    added_char.add(ordE('i'))
                    added_char.add(ordE('j'))
                else:
                    matrix[i][j] = alpha
                    added_char.add(alpha)
                alpha += 1
    return matrix



#
# def decrypt(key, text):
#     plain_text = ""
#     for letter in text:
#         if letter.isalpha():
#
#         else:
#             plain_text += letter
#     return plain_text

text = "the key is hidden under the door pad"
matrix = createMatrix("guidance")
print(matrix)
cipher_text = encrypt(matrix, text)
print("Original Text:", text)
print("Encrypted Text:", cipher_text)
# print("Decrypted Text:", decrypt(key, cipher_text))
