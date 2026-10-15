"""
Text Analysis and Word-Frequency Program

Purpose:
    Accepts a paragraph from the user, normalizes it (lower case, no
    punctuation, no extra spaces), splits it into words and displays:
    total words, unique words, words with more than 5 characters, number
    of vowels, the longest word, the frequency of every word and the
    words that occur more than once. Works for any paragraph entered.
"""
from collections import defaultdict

text = input("Enter a paragraph: ")

# ---- Normalize the text ----
text = text.lower().strip()                  # consistent case, remove end spaces
for ch in ".,!?;:\"'()-":                    # remove common punctuation marks
    text = text.replace(ch, "")
words = text.split()                         # split() also removes extra spaces

if len(words) == 0:
    exit("No words entered!")

# ---- Analysis ----
unique_words = set(words)                                # set -> unique words
long_words = [w for w in words if len(w) > 5]            # list comprehension
vowels = sum(text.count(v) for v in "aeiou")             # count() string method

freq = defaultdict(int)       # default dictionary: missing key starts at 0
longest = ""
for w in words:               # loop through all words
    freq[w] += 1              # no need to check whether the key exists
    if len(w) > len(longest):
        longest = w

# ---- Display ----
print("\nTotal words:", len(words))
print("Unique words:", len(unique_words))
print("Words with more than 5 characters:", len(long_words), long_words)
print("Number of vowels:", vowels)
print("Longest word:", longest)

print("\nWord frequencies:")
for word, count in freq.items():
    print(f"{word:<15}: {count}")

repeated = [w for w, c in freq.items() if c > 1]
print("\nWords occurring more than once:", repeated)