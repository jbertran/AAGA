def find_mu_lambda(seed, f):
    x = f(seed)
    y = f(f(seed))
    while x != y:
        x = f(x)
        y = f(f(x))
    lbd = 1
    x = f(x)
    y = f(f(y))
    while x != y:
        x = f(x)
        y = f(f(y))
        lbd += 1
    
    
