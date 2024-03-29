from point import Point


class Problem(object):

    def __init__(self, area_map, initial_state, goal_state):
        self.map = area_map
        self.dimensions = self.map.shape
        self.initial = initial_state
        self.goal = goal_state
        self.directions = ((0, -1),
                           (0, 1),
                           (-1, 0),
                           (1, 0),
                           (-1, -1),
                           (-1, 1),
                           (1, -1),
                           (1, 1),
                           )

    def goal_test(self, state):
        return self.goal == state

    def __available(self, state, x, y):
        new_x = state.x + x
        new_y = state.y + y

        height, width = self.map.shape
        if new_x < 0 or new_x >= height or new_y < 0 or new_y >= width:
            return False

        if self.map[new_x][new_y] == '@':
            return False

        # Check diagonals
        if x != 0 and y != 0:
            if self.map[state.x][new_y] == '@' or \
               self.map[new_x][state.y] == '@':
                return False

        return True

    def get_actions(self, state):
        return [Point(i, j) for i, j in self.directions
                if self.__available(state, i, j)]

    def result(self, parent_state, action):
        return parent_state + action

    def step_cost(self, parent_state, action):
        return 1 if action.x == 0 or action.y == 0 else 1.5
