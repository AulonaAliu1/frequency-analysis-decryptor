from collections import Counter

with open("encrypted.txt", "r", encoding="utf-8") as file:
    cipher = file.read()


english_freq = "etaoinshrldmucyfwgbpvkzjq"

letters = [c.lower() for c in cipher if c.isalpha()]

freq = Counter(letters)

sorted_letters = [item[0] for item in freq.most_common()]
mapping = {}

for i, letter in enumerate(sorted_letters):
    if i < len(english_freq):
        mapping[letter] = english_freq[i]

decrypted = ""

for c in cipher:
    if c.lower() in mapping:
        if c.isupper():
            decrypted += mapping[c.lower()].upper()
        else:
            decrypted += mapping[c.lower()]
    else:
        decrypted += c


print("\nFrequency table:")
print(freq)

print("\nGuessed mapping:")
print(mapping)

print("\nPossible decrypted text:")
print(decrypted)
