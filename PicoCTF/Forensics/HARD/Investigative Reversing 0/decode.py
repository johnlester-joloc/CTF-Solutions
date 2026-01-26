text = "picoCTK.k5zsid6q_f0a9b767}"

decoded_chars = []

decoded_chars[0:4] = text[0:4] # 'pico'
decoded_chars[4:6] = text[4:6] # 'CT'

for i in range(6, 15):
    decoded_chars.append(chr(ord(text[i]) - 5))

decoded_chars.append(chr(ord(text[15]) + 3))
for i in range(16, 26):
    decoded_chars.append(text[i])

print("".join(decoded_chars))