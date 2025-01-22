import asyncio as asy
from qbreader import Async as qba

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
                        "Compilation",]:
            if "Dynasty" not in auth and "BC" not in auth:
                fauths.append(auth.strip())
    #print(fauths)

relevs = []
async def verify(author, client):
    # await asy.sleep(0.001)
    resp = await client.query(
        queryString=author,
        difficulties=[0, 1, 2, 3, 4, 5],
        categories="Literature")
    return resp.tossups > 4 or resp.bonuses > 4

async def main():
    try: 
        client = await qba.create()
        tasks = [verify(author, client) for author in fauths]
        results = await asy.gather(*tasks)
        for author, relevant in zip(fauths, results):
            if relevant:
                relevs.append(author)
    finally:
        await client.close()
asy.run(main())
print(len(relevs))