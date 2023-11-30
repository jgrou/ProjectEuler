import math

with open('words.txt') as f:
    words = f.read()
   
words = words.replace('"', '').split(",")

def Anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    
    # Create dictionaries to count digit occurrences
    count1 = {}
    count2 = {}
    
    for letter in word1:
        count1[letter] = count1.get(letter, 0) + 1
    
    for letter in word2:
        count2[letter] = count2.get(letter, 0) + 1

    return count1 == count2

anagram_word_pairs = []

for i, word in enumerate(words):
    for second_word in words[i+1:]:
        if Anagram(word, second_word):
            anagram_word_pairs.append([word, second_word])

square_anagrams = []

# Neither may a different letter have the same digital value as another letter.
def Check(word,number):
    for i in range(len(word)):
        for j in range(i+1, len(word)):
            if word[i] == word[j]:
                if number[i] != number[j]:
                    return False
            else:
                if number[i] == number[j]:
                    return False
    return True
    
for [word1, word2] in anagram_word_pairs:
    length = len(word1)
    lower_bound = math.ceil(10**((length-1)/2))
    upper_bound = math.ceil(10**(length/2))
    for n in range(lower_bound, upper_bound):
        number = str(n**2)
        
        if Check(word1, number):
    
            new_number = ''
            
            for i in range(len(word1)):
                new_number += number[word1.index(word2[i])]
            if int(new_number)**0.5 % 1 == 0 and new_number[0] != '0':
                square_anagrams.append(int(new_number))
                square_anagrams.append(int(number))
            
answer = max(square_anagrams)