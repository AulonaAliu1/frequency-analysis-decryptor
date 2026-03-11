from collections import Counter

cipher = input("Enter the encrypted text:\n")

english_freq = "etaoinshrdlcumwfgypbvkjxqz"

letters = [c.lower() for c in cipher if c.isalpha()]

freq = Counter(letters)

sorted_letters = [item[0] for item in freq.most_common()]

print("\nFrequency table:")
print(freq)

print("\nGuessed mapping:")
print(mapping)

print("\nPossible decrypted text:")
print(decrypted)