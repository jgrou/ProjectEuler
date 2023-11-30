def SameDigits(a,b):
    for i in str(a):
        if i not in str(b):
            return False
    for i in str(b):
        if i not in str(a):
            return False
    return True
  
x = 0  
    
while True:
    x += 1
    if SameDigits(x, 2*x):
        if SameDigits(x, 3*x):
            if SameDigits(x, 4*x):
                if SameDigits(x, 5*x):
                    if SameDigits(x, 6*x):
                        break