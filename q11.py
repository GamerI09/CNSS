# Bit Stuffing

A = "01000111"
B = "11100011"
ESC = "11100000"
FLAG = "01111110"

frame = A + B + ESC + FLAG

# SENDER
result = ""
count = 0

for bit in frame:
    result += bit

    if bit == '1':
        count += 1
        if count == 5:
            result += '0'
            count = 0
    else:
        count = 0

result = FLAG + result + FLAG

print("Transmitted Frame:", result)


# RECEIVER
received = result

data = received[8:-8]

original = ""
count = 0
i = 0

while i < len(data):
    bit = data[i]
    original += bit

    if bit == '1':
        count += 1

        if count == 5:
            i += 1  # Skip stuffed zero
            count = 0
    else:
        count = 0

    i += 1

print("Received Data:", original)

print("A:", original[0:8])
print("B:", original[8:16])
print("ESC:", original[16:24])
print("FLAG:", original[24:32])
