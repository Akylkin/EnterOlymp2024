from collections import deque
scobkastr = '[{(({}){}])}]'
def correct(str):
    counter = 0
    deck = deque()
    deck1 = deque()
    deck2 = deque()
    for scobka in str:
        if scobka == '(':
            deck.append(scobka)
        if scobka == ')':
            if len(deck) != 0:
                deck.pop()
            else:
                counter += 1
        if scobka == '{':
            deck1.append(scobka)
        if scobka == '}':
            if len(deck1) != 0:
                deck1.pop()
            else:
                counter += 1
        if scobka == '[':
            deck2.append(scobka)
        if scobka == ']':
            if len(deck2) != 0:
                deck2.pop()
            else:
                counter += 1
    if counter == 0:
        return 'NICEEEE'
    else:
        return 'NO NO NO'

print(correct(scobkastr))