#!/usr/bin/python3
"""Solves the lock boxes puzzle """

def canUnlockAll(boxes):
    """Looks for the next opened box
    Args:
        opened_boxes (dict): Dictionary which contains boxes already opened
    Returns:
        list: List with the keys contained in the opened box
    """
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

def main():
    """Entry point"""
    canUnlockAll([[]])


if __name__ == '__main__':
    main()