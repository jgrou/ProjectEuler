with open('cipher.txt') as f:
    cipher = f.read()
cipher = cipher.split(",")

alphabet = [i for i in 'abcdefghijklmnopqrstuvwxyz']

for a in alphabet:
    for b in alphabet:
        for c in alphabet:
            DecryptedText = len(cipher) * [None]
            EncryptionKey = [ord(a),ord(b),ord(c)]
            Nonsense = False
            ans = 0
            
            for i, letter in enumerate(cipher):
                new_letter = int(letter) ^ EncryptionKey[i%3]
                if new_letter < 32 or new_letter > 122:
                    Nonsense = True
                    break
                ans += new_letter
                DecryptedText[i] = chr(new_letter)
                
            if not Nonsense:
                text = ''
                for i in DecryptedText:
                    text += i
                if 'the' in text:        
                    print(text)
                    print(ans)