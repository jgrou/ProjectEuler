with open('keylog.txt') as f:
    keylog = f.read()
   
keylog = [int(i) for i in keylog.split('\n')]
keylog.sort()
keylog = set(keylog) # Only unique elements necessary