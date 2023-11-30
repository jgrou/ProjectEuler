def multiply(x,y):
    return x * y

def plus(x,y):
    return x + y

def divide(x,y):
    if y == 0:
        return 2**0.5 # return irrational number so the answer will never be integer
    return x/y

def minus(x,y):
    return x - y

lst = [multiply, plus, divide, minus]

def Targets(numbers):
    ans = []
    for a in numbers:
        for b in numbers:
            if b != a:
                for c in numbers:
                    if c != b and c != a:
                        for d in numbers:
                            if d != a and d != b and d != c:
                                for e in lst:
                                    for f in lst:
                                        for g in lst:
                                            target = []
                                            target.append(g(f(e(a,b),c),d))
                                            target.append(g(f(e(b,a),c),d))
                                            target.append(g(f(c,e(a,b)),d))
                                            target.append(g(f(c,e(b,a)),d))
                                            target.append(g(d,f(e(a,b),c)))
                                            target.append(g(d,f(e(b,a),c)))
                                            target.append(g(d,f(c,e(a,b))))
                                            target.append(g(d,f(c,e(b,a))))
                                            for t in target:
                                                if t%1 == 0 and t > 0:
                                                    ans.append(t)
    return set(ans)

def Check(n, numbers):
    for i in range(n, 0, -1):
        if i not in numbers:
            return False
    return True
    
n_max = 1

for n1 in range(1,7):
    for n2 in range(n1,8):
        for n3 in range(n2,9):
            for n4 in range(n3,10):
                targets = Targets([n1,n2,n3,n4])
                if Check(n_max, targets):
                    answer = [n1,n2,n3,n4]
                    while n_max in targets:
                        n_max += 1