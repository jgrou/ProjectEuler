with open('words.txt') as f:
    words = f.read()
   
words = words.replace('"', '').split(",")

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
values = range(1,27)
dic = dict(zip(alphabet,values))

TriangleNumbers = [1]
t = 1
n = 2
ans = 0

while t < max([len(word) for word in words])*26:
    t =int(0.5 * n * (n + 1))
    TriangleNumbers.append(t)
    n += 1
   
for i, word in enumerate(words):
    AlphabeticalValue = 0
    for letter in word:
        AlphabeticalValue += dic[letter]
    if AlphabeticalValue in TriangleNumbers:
        ans += 1