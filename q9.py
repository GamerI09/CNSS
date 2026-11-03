A = "01000111"
B = "11100011"
ESC = "11100000"
FLAG = "01111110"

# SENDER
frame = [A, B, ESC, FLAG]

count = len(frame) + 1

result = format(count, '08b')

for byte in frame:
    result += byte

print("Transmitted Frame:", result)


# RECEIVER
received = result

count = int(received[:8], 2)

data = received[8:count*8]

print("Character Count:", count)
print("Received Data:")

for i in range(0, len(data), 8):
    print(data[i:i+8])
