with open('names.txt') as f:
    names = f.read()
   
names = names.replace('"', '').split(",")
names.sort()

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
values = range(1,27)
dic = dict(zip(alphabet,values))
ans = 0
    
for i, name in enumerate(names):
    AlphabeticalValue = 0
    for letter in name:
        AlphabeticalValue += dic[letter]
    ans += (i+1) * AlphabeticalValue