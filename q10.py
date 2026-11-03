# Byte Stuffing (Character Stuffing)

A = "01000111"
B = "11100011"
FLAG = "01111110"
ESC = "11100000"

frame = [A, B, ESC, FLAG]

# SENDER
result = FLAG

for byte in frame:
    if byte == FLAG or byte == ESC:
        result += ESC
    result += byte

result += FLAG

print("Transmitted Frame:", result)


# RECEIVER
received = result

data = received[8:-8]

original = []
i = 0

while i < len(data):
    byte = data[i:i+8]

    if byte == ESC:
        i += 8
        byte = data[i:i+8]

    original.append(byte)
    i += 8

print("Received Data:")

for byte in original:
    print(byte)
