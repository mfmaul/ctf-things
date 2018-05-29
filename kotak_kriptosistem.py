def maps(le):
    mapp = []
    for x in range(le):
        mapp.append(['.','.','.','.','.'])
    return mapp

def crypt(s, l, mep):
    g = 0
    h = 0
    for x in range(l):
        g = (ord(s[x])*7)/5
        h = (ord(s[x])*7)%5
        mep[x][h] = g
    return mep

def main():
    strs = raw_input("Give it a try : ")
    lens = len(strs)
    enc = crypt(strs, lens, maps(lens))
    for x in range(len(enc)):
        for y in range(5):
            print enc[x][y],
        print
      
if __name__ == "__main__":
    main()
