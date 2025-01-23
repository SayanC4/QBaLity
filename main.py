import asyncio as asy
from qbreader import Async

with open("./Those who Grow.txt") as lit:
    ls = lit.readlines()
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

# relevs = []
async def verify(author, client):
    await asy.sleep(0.001)
    resp = await client.query(
        queryString=author,
        difficulties=[0, 1, 2, 3, 4, 5],
        categories="Literature")
    return resp.tossups_found > 4 or resp.bonuses_found > 4

async def main():
    client = await Async.create()
    relevs = open("./relevance.txt", 'w')
    irrelevs = open("./irrelevance.txt", 'w')
    for author in fauths:
        relevance = await verify(author, client)
        print(f"{author}: {relevance}")
        relevs.write(f"{author}\n") if relevance else irrelevs.write(f"{author}\n")
    """
    tasks = [verify(author, client) for author in fauths]
    results = await asy.gather(*tasks)
    for author, relevant in zip(fauths, results):
        if relevant:
            relevs.append(author)
    """
    await client.close()
    relevs.close()
    irrelevs.close()
   
asy.run(main())