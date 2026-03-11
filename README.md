
Substitution Cipher Decryption using Frequency Analysis
Description

This Python program attempts to decrypt a substitution cipher using frequency analysis. Frequency analysis is a cryptographic technique that counts how often each letter appears in an encrypted text and compares it with the known frequency of letters in the English language. 
The program guesses which encrypted letters correspond to real letters by matching the most frequent letters in the ciphertext with the most common letters in English.

How It Works

The user enters an encrypted text.
The program counts the frequency of each letter.
Letters are sorted from most common to least common.
The program compares them with English letter frequency (etaoinshrdlcumwfgypbvkjxqz).
A guessed substitution mapping is created.
The program outputs a possible decrypted text.

Why Results May Not Be Perfect

The result is only a guess because:
the ciphertext may be too short
uncommon letter patterns may appear
substitution mappings may not match perfectly
Frequency analysis works better with longer texts because letter patterns become clearer.
