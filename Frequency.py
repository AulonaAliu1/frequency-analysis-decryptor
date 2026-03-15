from collections import Counter

cipher = input("Enter the text to generate the fequency:\n")


letters = [c.lower() for c in cipher if c.isalpha()]

freq = Counter(letters)

sorted_letters = [item[0] for item in freq.most_common()]
mapping = {}

print(sorted_letters)
