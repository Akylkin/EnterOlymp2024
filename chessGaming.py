def rturn(kp, rp, rt):
    if kp == rt or kp == rp :
        print('illegal move')
    check = 0
    kup = kp - 8
    kdown = kp + 8
    kleft = kp - 1
    kright = kp + 1
    rtinmoment = rt
    while (check != 1):
        bc = rtinmoment
        while (rtinmoment-8 > 0):
            rtinmoment -= 8
            if rtinmoment == kp:
                print('illegal state')
                rp += 1
        rtinmoment = bc
        while (rtinmoment+8 < 63):
            rtinmoment -= 8
            if rtinmoment == kp:
                print('illegal state')
                rp += 1
        rtinmoment = bc
        while (rtinmoment % 8 == 0):
            rtinmoment -= 1
            if rtinmoment == kp:
                print('illegal state')
                rp += 1
        rtinmoment = bc
        while ((rtinmoment + 1) % 8 > 0):
            rtinmoment += 1
            if rtinmoment == kp:
                print('illegal state')
                rp += 1
        rtinmoment = bc
