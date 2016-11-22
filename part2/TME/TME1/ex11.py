def neumann(n):
    sq = n*n
    strsq = str(sq)
    if len(strsq) != 20:
        strsq = (20-len(strsq))*'0' + strsq
    r = int(strsq[5:15])
    return r

def list_seen():
    seen = {}
    n = 100000
    while True:
        n = neumann(n)
        seen[n] = True
        if seen.get(n) is not None:
            break
    return [k for k, v in seen.items()]

if __name__ == '__main__':
    # Ex 1.1.1
    print(neumann(1234567890) == 1578750190)
    print(neumann(1010101010))

    # Ex 1.1.2
    print(list_seen())

    # Ex 1.1.4
    n = 1234567890
    l = [1234567890]
    for i in range(10):
        n = neumann(n)
        l.append(n)
    print(l)
        
