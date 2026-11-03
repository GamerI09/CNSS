def generate_matrix(key):
    key = key.lower().replace('j', 'i')
    matrix = []
    used = set()
    for char in key:
        if char.isalpha() and char not in used:
            used.add(char)
            matrix.append(char)
    for char in "abcdefghijklmnopqrstuvwxyz":
        if char == 'j':
            continue
        if char not in used:
            used.add(char)
            matrix.append(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == char:
                return r, c
    return None

def prepare_text(text):
    text = text.lower().replace(' ', '').replace('j', 'i')
    digraphs = []
    i = 0
    while i < len(text):
        c1 = text[i]
        if i + 1 < len(text):
            c2 = text[i+1]
            if c1 == c2:
                digraphs.append((c1, 'x'))
                i += 1
            else:
                digraphs.append((c1, c2))
                i += 2
        else:
            digraphs.append((c1, 'x'))
            i += 1
    return digraphs

def encrypt(text, key):
    matrix = generate_matrix(key)
    digraphs = prepare_text(text)
    cipher = []
    for c1, c2 in digraphs:
        r1, col1 = find_position(matrix, c1)
        r2, col2 = find_position(matrix, c2)
        if r1 == r2:  # Same row: shift right
            cipher.append(matrix[r1][(col1 + 1) % 5])
            cipher.append(matrix[r2][(col2 + 1) % 5])
        elif col1 == col2:  # Same column: shift down
            cipher.append(matrix[(r1 + 1) % 5][col1])
            cipher.append(matrix[(r2 + 1) % 5][col2])
        else:  # Rectangle: swap columns
            cipher.append(matrix[r1][col2])
            cipher.append(matrix[r2][col1])
    return ''.join(cipher)

def decrypt(cipher, key):
    matrix = generate_matrix(key)
    plain = []
    for i in range(0, len(cipher), 2):
        c1, c2 = cipher[i], cipher[i+1]
        r1, col1 = find_position(matrix, c1)
        r2, col2 = find_position(matrix, c2)
        if r1 == r2:  # Same row: shift left
            plain.append(matrix[r1][(col1 - 1) % 5])
            plain.append(matrix[r2][(col2 - 1) % 5])
        elif col1 == col2:  # Same column: shift up
            plain.append(matrix[(r1 - 1) % 5][col1])
            plain.append(matrix[(r2 - 1) % 5][col2])
        else:  # Rectangle: swap columns
            plain.append(matrix[r1][col2])
            plain.append(matrix[r2][col1])
    return ''.join(plain)

# Given input from practical question
plain_text = "the key is hidden under the door pad"
secret_key = "guidance"

matrix = generate_matrix(secret_key)
cipher_text = encrypt(plain_text, secret_key)
decrypted_text = decrypt(cipher_text, secret_key)

print("--- Playfair Cipher ---")
print("Secret Key  :", secret_key)
print("5x5 Matrix  :")
for row in matrix:
    print(" ", " ".join(row))
print("Plain Text  :", plain_text)
print("Encrypted   :", cipher_text)
print("Decrypted   :", decrypted_text)
