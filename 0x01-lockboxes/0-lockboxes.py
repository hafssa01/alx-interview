def canUnlockAll(boxes):
    n = len(boxes)

    unlocked = [False] * n
    unlocked[0] = True

    keys = [0]

    while keys:
        key = keys.pop()

        if not unlocked[key]:
            unlocked[key] = True

            for k in boxes[key]:
                if k < n and not unlocked[k]:
                    keys.append(k)
                
    return all(unlocked)