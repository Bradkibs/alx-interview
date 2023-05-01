#!/usr/bin/python3
"""a method that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """set to keep track of which boxes are unlocked"""
    unlocked = {0}
    # queue to keep track of the boxes to be opened
    queue = [0]

    while queue:
        box = queue.pop(0)
        # loop through all the keys in the current box
        for key in boxes[box]:
            # check if the key opens a box that has not been unlocked yet
            if key < len(boxes) and key not in unlocked:
                # add the box to the set of unlocked boxes
                unlocked.add(key)
                # add the box to the queue of boxes to be opened
                queue.append(key)

    # check if all boxes have been unlocked
    return len(unlocked) == len(boxes)
