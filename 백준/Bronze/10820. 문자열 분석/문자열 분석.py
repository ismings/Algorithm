while True:
    try:
        ans = [0]*4
        for s in input():
            i = ord(s)
            if i >= ord('a') and i <= ord('z'):
                ans[0] += 1
            elif i >= ord('A') and i <= ord('Z'):
                ans[1] += 1
            elif i >= ord('0') and i <= ord('9'):
                ans[2] += 1
            elif i == ord(' '):
                ans[3] += 1
        print(' '.join(map(str,ans)))
    except:
        break