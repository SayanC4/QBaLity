import json, random

""" Schema
{
   "title": {
        "author": "",
        "clues": [
            ""
        ], "protagonist": "", 
        "tags": []
    }
}
"""

with open("./cards.json", 'r') as file:
    cards = json.load(file)
    print(f"{len(cards)} cards.")
    titles = list(cards.keys())
    #random.shuffle(titles)
    questions: list[tuple] = []
    for i, title in enumerate(titles):
        card = cards[title]
        answer = f"{title} by {card["author"]}"
        questions.extend((c, answer) for c in card["clues"])
    random.shuffle(questions)
    cnt = 0
    while cnt < len(questions):
        print(f"Q{cnt + 1} of {len(questions)}")
        print(questions[cnt][0])
        nx = input("[A/N]: ").lower()
        if nx == 'a':
            print(questions[cnt][1])
            nx = input("[N/Q]: ").lower()
            if nx == 'q':
                cnt = len(questions)
        cnt += 1