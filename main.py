import asyncio as asy
from qbreader import Async

with open("./relevance.txt") as auths:
    fauths = auths.readlines()
    """
    filt = [l.strip() for l in ls if " -" in l]
    fauths = ["Saint-John Perse"]
    for f in filt:
        auth = f[:f.index('-')]
        if '(' in auth:
            auth = auth[:auth.index('(')]
        auth = auth.strip()
        if auth not in ["Unknown", 
                        "Anonymous", 
                        "Cyclic poets",
                        "Collected stories",
                        "Compilation",
                        "St."]:
            if "Dynasty" not in auth and "BC" not in auth:
                fauths.append(auth.strip())
    #print(fauths)
    """

# relevs = []
async def acount(author, client):
    await asy.sleep(0.001)
    qstr = ".*".join([f"\\b{w}\\w*\\b" for w in author.split()])
    # e.g. \bT\w*\b.*\bEliot\w*\b
    resp = await client.query(
        queryString=qstr,
        searchType="answer",
        regex=True,
        difficulties=[3, 4, 5],
        categories="Literature")
    return resp.tossups_found + resp.bonuses_found

async def main():
    client = await Async.create()
    asorted = open("./authsorted.txt", 'w')
    #irrelevs = open("./irrelevance.txt", 'w')
    adict = dict()
    for author in fauths:
        count = await acount(author, client)
        #print(f"{author}: {relevance}")
        #relevs.write(f"{author}\n") if relevance else irrelevs.write(f"{author}\n")
        adict[author.strip()] = count
        print(f"{author.strip()}:\t{count}")
    """
    tasks = [verify(author, client) for author in fauths]
    results = await asy.gather(*tasks)
    for author, relevant in zip(fauths, results):
        if relevant:
            relevs.append(author)
    """
    await client.close()
    lsort = sorted(adict.items(), key=lambda i: i[1], reverse=True)
    for a in lsort:
        asorted.write(f"{a[0]:<32}{a[1]}\n")
    #relevs.close()
    asorted.close()
asy.run(main())