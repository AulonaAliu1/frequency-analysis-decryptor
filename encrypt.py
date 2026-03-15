alphabet = "abcdefghijklmnopqrstuvwxyz"
substitute = "twerqyuiopasdfghjklzxcvbnm"

mapping = {}

for i in range(len(alphabet)):
    mapping[alphabet[i]] = substitute[i]

with open("text.txt", "r", encoding="utf-8") as file:
    cipher = file.read()

result = ""

for c in cipher:
    if c.lower() in mapping:
        if c.isupper():
            result += mapping[c.lower()].upper()
        else:
            result += mapping[c.lower()]
    else:
        result += c

with open("encrypted.txt", "w", encoding="utf-8") as file:
    file.write(result)

print("Encryption complete.")
print("Encrypted text saved to encrypted.txt")