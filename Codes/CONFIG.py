LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3

ACTIONS = [LEFT,DOWN,RIGHT,UP]

REPS = 20
EPISODES = 4000
EPSILON = 0.1
LEARNING_RATE = 0.1
DISCOUNT = 0.9
STUDENT_NUM = 810199165

FAIL_REWARD = -10
MOVE_REWARD = -1
GOAL_REWARD = 50

BEST_POLICY = {
    (0, 0): 2,
    (0, 1): 1,
    (0, 2): 1,
    (0, 3): 0,
    (1, 0): 2,
    (1, 1): 1,
    (1, 2): 1,
    (1, 3): 1,
    (2, 0): 2,
    (2, 1): 2,
    (2, 2): 2,
    (2, 3): 1,
    (3, 0): 2,
    (3, 1): 2,
    (3, 2): 2
}