with open('./authsorted.txt', 'r') as rf:
    auths = rf.readlines()
    stars = []
    i = 0
    while(i < len(auths)):
        if auths[i][0] == "*":
            stars.append(auths.pop(i)[1:])
        else:
            i += 1
    stars.extend(auths)
with open('./resorted.txt', 'w') as wf:
    for s in stars:
        wf.write(s)