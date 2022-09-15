import numpy as np


def draw_policy(policy):
    arrows = {
        0: '←', 
        1: '↓', 
        2: '→', 
        3: '↑', 
        -1: '↻'
    }
    for i in range(4):
        ids = []
        for j in range(4):
            if (i, j) == (3, 3):
                ids.append(-1)
            else:
                idx = np.argmax(policy[(i, j)])
                ids.append(idx)
        print('|'.join([arrows[id_] for id_ in ids]))