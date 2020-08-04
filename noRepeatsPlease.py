def perm(str):
    def fact(n):
        return 1 if n==0 else n*fact(n-1)

    p = [[str[0]] for i in range(fact(len(str)-1))]

    for i in range(len(p)):
        p[i].append(str[1])

    print(p)

print(perm('12345'))
