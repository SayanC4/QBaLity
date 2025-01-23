#import asyncio
#from qbreader import Async
import random

if __name__ == "__main__":
    with open("./todo.txt", 'w') as writefile:
        readfile = open("./relevance.txt", 'r')
        authors = readfile.readlines()
        readfile.close()
        random.shuffle(authors)
        for author in authors:
            writefile.write(f"{author}")
