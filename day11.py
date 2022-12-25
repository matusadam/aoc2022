

def load():
    # I didn't write a parser for this challenge
    return [
    # 0
    { 
        "items" : [59, 74, 65, 86],
        "op" : lambda old: old * 19,
        "test" : 7,
        "true" : 6,
        "false" : 2,
        "inspects" : 0,
    },
    # 1
    {
        "items" : [62, 84, 72, 91, 68, 78, 51],
        "op" : lambda old: old + 1,
        "test" : 2,
        "true" : 2,
        "false" : 0,
        "inspects" : 0,
    },
    # 2
    {
        "items" : [78, 84, 96],
        "op" : lambda old: old + 8,
        "test" : 19,
        "true" : 6,
        "false" : 5,
        "inspects" : 0,
    },
    # 3
    {
        "items" : [97, 86],
        "op" : lambda old: old * old,
        "test" : 3,
        "true" : 1,
        "false" : 0,
        "inspects" : 0,
    },
    # 4
    {
        "items" : [50],
        "op" : lambda old: old + 6,
        "test" : 13,
        "true" : 3,
        "false" : 1,
        "inspects" : 0,
    },
    # 5
    {
        "items" : [73, 65, 69, 65, 51],
        "op" : lambda old: old * 17,
        "test" : 11,
        "true" : 4,
        "false" : 7,
        "inspects" : 0,
    },
    # 6
    {
        "items" : [69, 82, 97, 93, 82, 84, 58, 63],
        "op" : lambda old: old + 5,
        "test" : 5,
        "true" : 5,
        "false" : 7,
        "inspects" : 0,
    },
    # 7
    {
        "items" : [81, 78, 82, 76, 79, 80],
        "op" : lambda old: old + 3,
        "test" : 17,
        "true" : 3,
        "false" : 4,
        "inspects" : 0,
    },
]

def solution(part):
    rounds = 20 if part==1 else 10000
    monkeys = load()
    tmod = 1
    for m in monkeys:
        tmod *= m['test']
    for _ in range(rounds):
        for m in monkeys:
            for item in m["items"]:
                m["inspects"] += 1
                item_val = m["op"](item)
                item_val %= tmod
                item_val = item_val // 3 if part==1 else item_val
                if item_val % m["test"] == 0:
                    monkeys[m["true"]]["items"].append(item_val)
                else:
                    monkeys[m["false"]]["items"].append(item_val)     
            m["items"] = []

    a,b = sorted(monkeys, key=lambda x: x["inspects"])[-2:]
    return a["inspects"] * b["inspects"]

print(solution(1))
print(solution(2))