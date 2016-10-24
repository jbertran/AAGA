def algok(x):
    y = x // 10 ** 9
    uglygotos = {}
    def two():
        switch = 3 + z
        uglygotos[switch]()
    def three():
        if x < 5e9:
            x = x + 5 * 10 ** 9
        uglygotos[4]()
    def four():
        x = (x ** 2 // 10 ** 5) % 10 ** 10
        uglygotos[5]()
    def five():
        x = (1001001001 * x) % 10 ** 10
        uglygotos[6]()
    def six():
        if x < 1e8:
                x = x + 9814055677
        else:
            x = 10 ** 10 - x
        uglygotos[7]()
    def seven():
        x = 10 ** 5 * (x % 10 ** 5) + (x // 10 ** 5)
        uglygotos[8]()
    def eight():
        x = (1001001001 * x) % 10 ** 10
        uglygotos[9]()
    def nine():
        strx = str(x)
        for i in range(len(strx)):
            if strx[i] != '0':
                strx[i] = str(int(strx[i]) - 1)
        x = int(strx)
        uglygotos[10]()
    def ten():
        if x < 1e5:
            x = x ** 2 + 99999
        else:
            x = x - 99999
        uglygotos[11]()
    def eleven():
        while x < 1e9:
            x = 10 * x
        uglygotos[12]()
    def twelve():
        x = (x * (x - 1) // 10 ** 5) % 10 ** 10
        uglygotos[2]()
    def thirteen():
        if  y > 0:
            y -= 1
            uglygotos[2]()
        else:
            return x

    uglygotos = {
        2: two,
        3: three,
        4: four,
        5: five,
        6: six,
        7: seven,
        8: eight,
        9: nine,
        10: ten,
        11: eleven,
        12: twelve,
        13: thirteen
    }

    while True:
        z = (x // 10 ** 8) % 10
        uglygotos[2]()
        
            
        
            
