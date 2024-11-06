sticklist = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
stickcount = []
maxstick = len(sticklist)

for stick in range(maxstick):
    count = 0
    if stick == 0:
        count += sticklist[0] + sticklist[1 * 2 - 1] * 2 + sticklist[1 * 2 + 1 - 1]
    elif stick * 2 >= len(sticklist):
        count += sticklist[stick * 2 - 1] + sticklist[stick * 2] * 2 + sticklist[stick]
    else:
        count += sticklist[stick] + sticklist[stick * 2 - 1] + sticklist[stick * 2] * 2 + sticklist[stick * 2 + 1]
    stickcount.append(count)

print(f'Max len = {max(stickcount)}, Max stick = {stickcount.index(max(stickcount)) + 1}')