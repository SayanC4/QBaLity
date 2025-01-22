with open("./Those who Grow.txt") as lit:
    ls = lit.readlines()
    filt = [l.strip() for l in ls if " -" in l]
    print(len(filt))
