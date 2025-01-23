import asyncio
from qbreader import Async

async def search_author_tossups(authors):
    # Initialize the asynchronous QBReader client
    client = await Async.create()
    for author in authors:
        # Perform the search
        query = {
            "queryString": author,
            "categories": ["Literature"],
            "difficulties": [1, 2, 3, 4, 5],
        }
        results = await client.query(**query)

        # Print the count of tossups for the author
        print(f"{author}: {results.tossups_found} tossups found.")
    await client.close()

if __name__ == "__main__":
    # Replace with the three author names you want to search for
    authors = ["William Shakespeare", "Jane Austen", "Mark Twain"]

    # Run the asynchronous search
    asyncio.run(search_author_tossups(authors))