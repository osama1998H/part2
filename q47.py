from typing import Counter
text = '''Write a Python program which reads a text only alphabetical characters and spaces. and prints two words. The first one is the word which is arise most frequently in the text. The second one is the word which has the maximum number of letters'''

text = text.lower()
words = text.split()
# print(words)
co = Counter(words)
print(co.most_common(1))
le = 0
for i in words:
    if len(i) > le:
        le = len(i)
        n = words.index(i)
print(words[n])
