from bisect import bisect_left, bisect_right

def double(l: list) -> bool:
    h=set()
    for nums in l:
        if nums in h:
            return True
        h.add(nums)
    return False

def suminset(l: list, num):
    h=set()
    for nums in l:
        if num - nums in h:
            return True
        h.add(nums)

def range(l: list, numa: int, numb:int) -> list:
    l.sort()
    answ = []
    ia = bisect_left(l, numa)
    ib = bisect_right(l, numb)
    while(ia != ib):
        answ.append(l[ia])
        ia += 1
    return answ

def longestmass(l: list)
        
    

