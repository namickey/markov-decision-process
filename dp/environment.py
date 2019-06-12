#coding: utf-8

class State():
    def __init__(self, row=-1, column=-1):
        self.row = row
        self.column = column
    def __repr__(self):
        return "<State: [{}, {}]".format(self.row, self.column)
    def clone(self):
        return State(self.row, self.column)
    def __hash__(self):
        return hash((self.row, self.column))
    def __eq__(self, other):
        return self.row == other.row and self.column == other.column

class Action(Enum):
    UP = 1
    DOWN = -1
    LEFT = 2
    RIGHT = -2

class Environment():
    def __init__(self, grid, move_prob=0.8):
        self.grid = grid
        self.agent_state = State()
        self.default_reward = -0.04
        self.move_prob = move_prob
        self.reset()

    @property
    def row_length(self):
        return len(self.grid)
