def triplepairless9() -> list:
    pairlist = []
    for i in range(1, 7):
        for i1 in range(1, 10):
            for i2 in range(1, 10):
                if i + i1 + i2 < 9:
                    pairlist.append(int(str(i) + str(i1) + str(i2)))
    return pairlist

def doublepairless9():
    pairlist = []
    for i in range(1, 7):
        for i1 in range(1, 10):
            if i + i1 < 9:
                pairlist.append(int(str(i) + str(i1)))
    return pairlist

def final20boss(listtrip: list, listdouble: list) -> int:
    counter = 0
    counter1 = 0
    for i in listtrip:
        for i1 in listdouble:
            for i2 in listtrip:
                nl = []
                for nums in str(i)+str(i1)+str(i2):
                    nl.append(int(nums))
                if (nl[1] + nl[2] + nl[3] < 9 and 
                    nl[2] + nl[3] + nl[4] < 9 and 
                    nl[3] + nl[4] + nl[5] < 9 and
                    nl[4] + nl[5] + nl[6] < 9):
                    counter += 1
    for i in listtrip:
        for i1 in listdouble:
            nl = []
            for nums in str(i)+str(i1):
                nl.append(int(nums))
            if (nl[1] + nl[2] + nl[3] < 9 and 
                nl[2] + nl[3] + nl[4] < 9):
                counter1 += 1
    return counter * counter * counter * counter1

print(final20boss(triplepairless9(), doublepairless9()))