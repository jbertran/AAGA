def neumann2(strn):
    n = int(strn)
    sq = n*n
    strsq = str(sq)
    if len(strsq) != 4:
        strsq = (4-len(strsq))*'0' + strsq
    r = strsq[1:3]
    return r

def list_seen2(strn):
    seen = {}
    while True: 
        if seen.get(strn) is not None:
            break
        seen[strn] = True
        strn = neumann2(strn)
    res = [k for k, v in seen.items()]
    return res 

def amount_have_00():
    res = []
    for i in range(10):
        for j in range(10):
            seed = str(i)+str(j)
            if '00' in list_seen2(seed):
                res.append(seed)
    return res

def best_seeds():
    max_seeds = []
    max_seeds_nb = 0
    for i in range(10):
        for j in range(10):
            seed = str(i)+str(j)
            nb_seeds = len(list_seen2(seed))
            if nb_seeds == max_seeds_nb:
                max_seeds.append(seed)
            elif nb_seeds > max_seeds_nb:
                max_seeds_nb = nb_seeds
                max_seeds = [seed]
    return (max_seeds, max_seeds_nb)

if __name__ == '__main__':
    # Ex. 1.2.2
    print(len(amount_have_00()))
    # Ex. 1.2.4
    print(best_seeds())
