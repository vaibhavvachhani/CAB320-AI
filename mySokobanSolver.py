
'''

    2019 CAB320 Sokoban assignment

The functions and classes defined in this module will be called by a marker script.
You should complete the functions and classes according to their specified interfaces.
You are not allowed to change the defined interfaces.
That is, changing the formal parameters of a function will break the
interface and triggers to a fail for the test of your code.

# by default does not allow push of boxes on taboo cells
SokobanPuzzle.allow_taboo_push = False
# use elementary actions if self.macro == False
SokobanPuzzle.macro = False
'''

# you have to use the 'search.py' file provided
# as your code will be tested with this specific file
import search

import sokoban
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def my_team():
    '''
    Return the list of the team members of this assignment submission as a list
    of triplet of the form (student_number, first_name, last_name)

    '''
#    return [ (1234567, 'Ada', 'Lovelace'), (1234568, 'Grace', 'Hopper'), (1234569, 'Eva', 'Tardos') ]
    return [ (9889132, 'Nok Hei Heidi', 'Cheng'), (10003665, 'Jayden', 'Dao'), (9796134, 'Vaibhav', 'Vachhani')]

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def surrounded_by_walls(walls, x_size, y_size, coord):

    '''
    Identifies the areas which is walkable from the intisial state of the worker.

    '''

    (x, y) = coord
    left = right = top = bottom = False
    #finding left
    for x1 in range(x-1, -1, -1):
        if (x1, y) in walls:
            left = True
            break
    #finding right
    for x1 in range(x+1, x_size):
        if (x1, y) in walls:
            right = True
            break
    #finding top
    for y1 in range(y-1, -1, -1):
        if (x, y1) in walls:
            top = True
            break
    #finding bottom
    for y1 in range(y+1, y_size):
        if (x, y1) in walls:
            bottom = True
            break
    if left == False or right == False or top == False or bottom == False:
        return False
    else:
        return True

def number_of_walls_surrounded(walls, coord):
    '''
    return number of walls around the worker

    @param wall: warehouse walls object
    @param coord: the state of the worker

    '''
    (x, y) = coord
    number_of_walls = 0
    if (x-1, y) in walls:
        number_of_walls += 1
    if (x+1, y) in walls:
        number_of_walls += 1
    if (x, y-1) in walls:
        number_of_walls += 1
    if (x, y+1) in walls:
        number_of_walls += 1
    return number_of_walls

def walls_around(walls, coord):
    '''
    return walls coordinate around the worker

    @param walls: wall object
    @param coord: the state of the worker

    '''
    (x, y) = coord
    walls_around = []
    if (x-1, y) in walls:
        walls_around.append((x-1, y))
    if (x+1, y) in walls:
        walls_around.append((x+1, y))
    if (x, y-1) in walls:
        walls_around.append((x, y-1))
    if (x, y+1) in walls:
        walls_around.append((x, y+1))
    return walls_around

def has_target(walls_around_list, walkable_coord, warehouse):
    '''
    return boolean if walls around the coordinate

    @param walls_around_list: coordinate of walls around list
    @param walkable_coord: coordinates which is walkable
    @param warehouse: a Warehouse object

    '''
    walls = warehouse.walls
    targets = warehouse.targets
    wall = walls_around_list[0]
    abs_wall_x = abs(wall[0] - walkable_coord[0])
    abs_wall_y = abs(wall[1] - walkable_coord[1]) 
    abs_wall_diff = (abs_wall_x, abs_wall_y)

    wall_x = wall[0] - walkable_coord[0]
    wall_y = wall[1] - walkable_coord[1]
    wall_diff = (wall_x, wall_y)
    if abs_wall_diff == (1, 0):
        # difference on the X axis
        near_wall_coord = (walkable_coord[0], walkable_coord[1] + 1)
        while near_wall_coord not in walls:
            num_of_walls = number_of_walls_surrounded(walls, near_wall_coord)
            if num_of_walls == 0:
                return True
            elif num_of_walls == 1:
                this_wall_diff_x = walls_around(walls, near_wall_coord)[0][0] - near_wall_coord[0]
                this_wall_diff_y = walls_around(walls, near_wall_coord)[0][1] - near_wall_coord[1]
                this_wall_diff = (this_wall_diff_x, this_wall_diff_y)
                if this_wall_diff != wall_diff:
                    return True
            if near_wall_coord in targets:
                return True
            near_wall_coord = (near_wall_coord[0], near_wall_coord[1] + 1)


        near_wall_coord = (walkable_coord[0], walkable_coord[1] - 1)
        while near_wall_coord not in walls: 
            num_of_walls = number_of_walls_surrounded(walls, near_wall_coord)
            if num_of_walls == 0:
                return True
            elif num_of_walls == 1:
                this_wall_diff_x = walls_around(walls, near_wall_coord)[0][0] - near_wall_coord[0]
                this_wall_diff_y = walls_around(walls, near_wall_coord)[0][1] - near_wall_coord[1]
                this_wall_diff = (this_wall_diff_x, this_wall_diff_y)
                if this_wall_diff != wall_diff:
                    return True
            if near_wall_coord in targets:
                return True
            near_wall_coord = (near_wall_coord[0], near_wall_coord[1] - 1)

    elif abs_wall_diff == (0, 1):
        # difference on the Y axis
        near_wall_coord = (walkable_coord[0] + 1, walkable_coord[1])
        while near_wall_coord not in walls:
            num_of_walls = number_of_walls_surrounded(walls, near_wall_coord)
            if num_of_walls == 0:
                return True
            elif num_of_walls == 1:
                this_wall_diff_x = walls_around(walls, near_wall_coord)[0][0] - near_wall_coord[0]
                this_wall_diff_y = walls_around(walls, near_wall_coord)[0][1] - near_wall_coord[1]
                this_wall_diff = (this_wall_diff_x, this_wall_diff_y)
                if this_wall_diff != wall_diff:
                    return True
            if near_wall_coord in targets: 
                return True
            near_wall_coord = (near_wall_coord[0] + 1, near_wall_coord[1])

        near_wall_coord = (walkable_coord[0] - 1, walkable_coord[1])
        while near_wall_coord not in walls:
            num_of_walls = number_of_walls_surrounded(walls, near_wall_coord)
            if num_of_walls == 0:
                return True
            elif num_of_walls == 1:
                this_wall_diff_x = walls_around(walls, near_wall_coord)[0][0] - near_wall_coord[0]
                this_wall_diff_y = walls_around(walls, near_wall_coord)[0][1] - near_wall_coord[1]
                this_wall_diff = (this_wall_diff_x, this_wall_diff_y)
                if this_wall_diff != wall_diff:
                    return True
            if near_wall_coord in targets:
                return True
            near_wall_coord = (near_wall_coord[0] - 1, near_wall_coord[1])
    return False
  
def number_of_taboo_surrounded(taboos, coord):
    '''
    return number of walls around the worker

    @param wall: warehouse walls object
    @param coord: the state of the worker

    '''
    (x, y) = coord
    number_of_taboos = 0
    if (x-1, y) in taboos:
        number_of_taboos += 1
    if (x+1, y) in taboos:
        number_of_taboos += 1
    if (x, y-1) in taboos:
        number_of_taboos += 1
    if (x, y+1) in taboos:
        number_of_taboos += 1
    return number_of_taboos

def taboo_cells(warehouse):
    '''
    Identify the taboo cells of a warehouse. A cell inside a warehouse is
    called 'taboo' if whenever a box get pushed on such a cell then the puzzle
    becomes unsolvable.
    When determining the taboo cells, you must ignore all the existing boxes,
    simply consider the walls and the target cells.
    Use only the following two rules to determine the taboo cells;
     Rule 1: if a cell is a corner inside the warehouse and not a target,
             then it is a taboo cell.
     Rule 2: all the cells between two corners inside the warehouse along a
             wall are taboo if none of these cells is a target.

    @param warehouse: a Warehouse object
    @return
       A string representing the puzzle with only the wall cells marked with
       an '#' and the taboo cells marked with an 'X'.
       The returned string should NOT have marks for the worker, the targets,
       and the boxes.
    '''
    # initialise the walls
    walls = warehouse.walls
    targets = warehouse.targets
    walls_X, walls_Y = zip(*walls)
    x_size, y_size = 1+max(walls_X), 1+max(walls_Y)

    # making a list of tuples with all coords
    new_coords = []
    for i in range(y_size):
        for j in range(x_size):
            new_coords.append((j, i))
    # filtering out walls
    for i in range(len(walls)):
        new_coords.remove(walls[i])

    # filtering out targets
    targets = warehouse.targets
    for i in range(len(targets)):
        new_coords.remove(targets[i])

    # filtering out outside map
    walkable_coords = new_coords.copy()
    for i in range(len(new_coords)):
        if surrounded_by_walls(walls, x_size, y_size, new_coords[i]) == False:
            walkable_coords.remove(new_coords[i])

    #finding taboo coords
    taboo_coords = []
    for walkable_coord in walkable_coords:
        number_of_walls = number_of_walls_surrounded(walls, walkable_coord)
        walls_around_list = walls_around(walls, walkable_coord)
        if number_of_walls > 2:
            taboo_coords.append(walkable_coord)
        elif number_of_walls == 1:
            if not has_target(walls_around_list, walkable_coord, warehouse):
                taboo_coords.append(walkable_coord)
        elif number_of_walls == 2:
            if walls_around_list[0][0] != walls_around_list[1][0] and walls_around_list[0][1] != walls_around_list[1][1]:
                taboo_coords.append(walkable_coord)

    for walkable_coord in walkable_coords:
        number_of_walls = number_of_walls_surrounded(walls, walkable_coord)
        walls_around_list = walls_around(walls, walkable_coord)
        number_of_taboos = number_of_taboo_surrounded(taboo_coords, walkable_coord)
        if number_of_walls == 2 and number_of_taboos == 2:
            taboo_coords.append(walkable_coord)
    global taboo_cells_list
    taboo_cells_list = taboo_coords
    # putting everything in output
    output = [[" "] * x_size for y in range(y_size)]
    for (x,y) in walls:
           output[y][x] = "#"
    for (x,y) in taboo_coords:
           output[y][x] = "X"
    return "\n".join(["".join(line) for line in output])

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


class SokobanPuzzle(search.Problem):
    '''
    An instance of the class 'SokobanPuzzle' represents a Sokoban puzzle.
    An instance contains information about the walls, the targets, the boxes
    and the worker.
    Your implementation should be fully compatible with the search functions of
    the provided module 'search.py'.

    Each instance should have at least the following attributes
    - self.allow_taboo_push
    - self.macro

    When self.allow_taboo_push is set to True, the 'actions' function should
    return all possible legal moves including those that move a box on a taboo
    cell. If self.allow_taboo_push is set to False, those moves should not be
    included in the returned list of actions.

    If self.macro is set True, the 'actions' function should return
    macro actions. If self.macro is set False, the 'actions' function should
    return elementary actions.


    '''
    #
    #         "INSERT YOUR CODE HERE"
    #
    #     Revisit the sliding puzzle and the pancake puzzle for inspiration!
    #
    #     Note that you will need to add several functions to
    #     complete this class. For example, a 'result' function is needed
    #     to satisfy the interface of 'search.Problem'.

    def __init__(self, warehouse):
        self.warehouse = warehouse
        self.initial = (warehouse.worker,) + tuple(warehouse.boxes) 
        self.goal = warehouse.targets
        # by default does not allow push of boxes on taboo cells
        self.allow_taboo_push = False
        # use elementary actions if self.macro == False
        self.macro = False
        taboo_cells(warehouse)
    
    # define the actions
    def actions_macro(self, state):
        '''
        return action as a direction in the (x, y) coordinate for macro

        @param state: coordinate of the worker and boxes

        '''
        workerState = state[0]
        boxesState = state[1:]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        directions_words = ['Left', 'Right', 'Up', 'Down']

        actions = []
        for boxState in boxesState:
            for dId, direction in enumerate(directions):
                # moves boxes in the before state
                before_box_x = boxState[0] + direction[0]
                before_box_y = boxState[1] + direction[1]
                before_box_state = (before_box_x, before_box_y)
                # moves boxes in the after state
                after_box_x = boxState[0] - direction[0]
                after_box_y = boxState[1] - direction[1]
                after_box_state = (after_box_x, after_box_y)
                if after_box_state in self.warehouse.walls or before_box_state in self.warehouse.walls:
                    continue
                if after_box_state in boxesState or before_box_state in boxesState:
                    continue
                if not self.allow_taboo_push:
                    if after_box_state in taboo_cells_list:
                        continue
                temp_warehouse = self.warehouse.copy(workerState, boxesState)
                if can_go_there(temp_warehouse, (before_box_state[1], before_box_state[0])):
                    actions.append(((boxState[1], boxState[0]), directions_words[dId]))
        return actions

            
    def actions_elementary(self, state):
        '''
        return action as a direction in the (x, y) coordinate for element

        @param state: the tuple coordinate of the worker and boxes

        '''
        workerState = state[0]
        boxesState = state[1:]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        directions_words = ['Left', 'Right', 'Up', 'Down']
        actions = []
        # checks if the working is going to collised into a wall or into another box
        for id, direction in enumerate(directions):
            new_worker_x = workerState[0] + direction[0]
            new_worker_y = workerState[1] + direction[1]
            new_worker = (new_worker_x, new_worker_y)
            if new_worker in self.warehouse.walls:
                continue
            # checks the box collision with the wall
            if new_worker in boxesState:
                new_box_x = new_worker_x + direction[0]
                new_box_y = new_worker_y + direction[1]
                new_box = (new_box_x, new_box_y)
                if new_box in self.warehouse.walls or new_box in boxesState:
                    continue
                # checks if the box is in a taboo cell
                if not self.allow_taboo_push:
                    if new_box in taboo_cells_list:
                        continue
            # allows the move
            actions.append(directions_words[id])
        return actions

    def actions(self, state):
        """
        Return the list of actions that can be executed in the given state.

        As specified in the header comment of this class, the attributes
        'self.allow_taboo_push' and 'self.macro' should be tested to determine
        what type of list of actions is to be returned.

        When self.allow_taboo_push is set to True, the 'actions' function should 
        return all possible legal moves including those that move a box on a taboo 
        cell. If self.allow_taboo_push is set to False, those moves should not be
        included in the returned list of actions.
    
        If self.macro is set True, the 'actions' function should return 
        macro actions. If self.macro is set False, the 'actions' function should 
        return elementary actions.
        """
        if self.macro == False:
            return self.actions_elementary(state)
        else:
            return self.actions_macro(state)

    def macro_result(self, state, action):
        '''
        return state the state after with actions for marco

        @param state: the tuple coordinate of the worker and boxes
        @param action: the direction of an action for the worker

        '''
        workerState = (action[0][1], action[0][0])
        boxesState = list(state[1:])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        directions_words = ['Left', 'Right', 'Up', 'Down']
        # moves the worker and boxes in the direction of the action
        for wordId, direction_word in enumerate(directions_words):
            if action[1] == direction_word:
                boxState_X = workerState[0] + directions[wordId][0]
                boxState_Y = workerState[1] + directions[wordId][1]
                new_boxState = (boxState_X, boxState_Y)
                boxesState.remove(workerState)
                boxesState.append(new_boxState)
                return (workerState,) + tuple(boxesState)
                
    def elem_result(self, state, action):
        '''
        return state the state after with actions for element

        @param state: the tuple coordinate of the worker and boxes
        @param action: the direction of an action for the worker
        
        '''
        workerState = state[0]
        boxesState = list(state[1:])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        directions_words = ['Left', 'Right', 'Up', 'Down']
        # moves the worker and boxes in the direction of the action
        for wordId, direction_word in enumerate(directions_words):
            if action == direction_word:
                workerState_X = workerState[0] + directions[wordId][0]
                workerState_Y = workerState[1] + directions[wordId][1]
                new_workerState = (workerState_X, workerState_Y)
                if new_workerState in boxesState:
                    boxState_X = workerState_X + directions[wordId][0]
                    boxState_Y = workerState_Y + directions[wordId][1]
                    new_boxState = (boxState_X, boxState_Y)
                    boxesState.remove(new_workerState)
                    boxesState.append(new_boxState)
                    return (new_workerState,) + tuple(boxesState)
                return (new_workerState,) + tuple(boxesState)

    def result(self, state, action):
        '''
        returns the state of the boxes and worker after action is performed

        @param state: the current state of worker and boxes
        @param action: a tuple of states of worker and boxes

        '''
        if not self.macro:
            return self.elem_result(state, action)
        else:
            return self.macro_result(state, action)
    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal, as specified in the constructor. Override this
        method if checking against a single self.goal is not enough."""
        for thisGoal in self.warehouse.targets:
            if thisGoal not in state[1:]:
                return False
        return True
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def check_action_seq(warehouse, action_seq):
    '''
    Determine if the sequence of actions listed in 'action_seq' is legal or not.

    Important notes:
      - a legal sequence of actions does not necessarily solve the puzzle.
      - an action is legal even if it pushes a box onto a taboo cell.

    @param warehouse: a valid Warehouse object
    @param action_seq: a sequence of legal actions.
           For example, ['Left', 'Down', Down','Right', 'Up', 'Down']

    @return
        The string 'Failure', if one of the action was not successul.
           For example, if the agent tries to push two boxes at the same time,
                        or push one box into a wall.
        Otherwise, if all actions were successful, return
               A string representing the state of the puzzle after applying
               the sequence of actions.  This must be the same string as the
               string returned by the method  Warehouse.__str__()
    '''

    # checks the previous action of the boxes
    for action in action_seq:
        if action == 'Left':
            warehouse.worker = (warehouse.worker[0] - 1, warehouse.worker[1])
        elif action == 'Right':
            warehouse.worker = (warehouse.worker[0] + 1, warehouse.worker[1])
        elif action == 'Up':
            warehouse.worker = (warehouse.worker[0], warehouse.worker[1] - 1)
        elif action == 'Down':
            warehouse.worker = (warehouse.worker[0], warehouse.worker[1] + 1)

        last_action = action_seq[-1]
        # checks if there are adjacent boxes position
        failure_boxes = []
        for i in range(2):
            if last_action == 'Left':
                failure_boxes.append((warehouse.worker[0] + i, warehouse.worker[1]))
            elif last_action == 'Right':
                failure_boxes.append((warehouse.worker[0] - i, warehouse.worker[1]))
            elif last_action == 'Up':
                failure_boxes.append((warehouse.worker[0], warehouse.worker[1] - i))
            elif last_action == 'Down':
                failure_boxes.append((warehouse.worker[0], warehouse.worker[1] + i))
        # worker walks in wall
        if warehouse.worker in warehouse.walls:
            return "Failure"
        # checks if they are adjenct
        if failure_boxes[0] in warehouse.boxes and failure_boxes[1] in warehouse.boxes:
            return "Failure"
        if failure_boxes[0] in warehouse.boxes:
            warehouse.boxes.remove(failure_boxes[0])
            warehouse.boxes.append(failure_boxes[1])
    return warehouse.__str__()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def solve_sokoban_elem(warehouse):
    '''
    This function should solve using elementary actions
    the puzzle defined in a file.

    @param warehouse: a valid Warehouse object
    @return
        If puzzle cannot be solved return the string 'Impossible'
        If a solution was found, return a list of elementary actions that solves
            the given puzzle coded with 'Left', 'Right', 'Up', 'Down'
            For example, ['Left', 'Down', Down','Right', 'Up', 'Down']
            If the puzzle is already in a goal state, simply return []
    '''
    
    problem = SokobanPuzzle(warehouse)

    def h(node):
        boxes = node.state[1:]
        goals = warehouse.targets
        total = 0
        for box in boxes:
            shortest = 10000000
            for goal in goals:
                # uses the manhattan distance
                xdist = abs(box[0] - goal[0])
                ydist = abs(box[1] - goal[1])
                distance = xdist + ydist
                if shortest == None or distance < shortest:
                    shortest = distance
            total = total + shortest
        return total

    #node = search.depth_first_graph_search(problem)
    #node = search.breadth_first_graph_search(problem)
    node = search.astar_graph_search(problem, h)
    #node = search.uniform_cost_search(problem)
    #node = search.breadth_first_tree_search(problem)

    # search function cant find a solution
    if node == None:
        return ["Impossible"]
    return node.solution()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class SokobanCanGoPuzzle(search.Problem):
    '''
    An instance of the class 'SokobanPuzzle' represents a Sokoban puzzle.
    An instance contains information about the walls, the targets, the boxes
    and the worker.
    Your implementation should be fully compatible with the search functions of
    the provided module 'search.py'.

    Each instance should have at least the following attributes
    - self.allow_taboo_push
    - self.macro

    When self.allow_taboo_push is set to True, the 'actions' function should
    return all possible legal moves including those that move a box on a taboo
    cell. If self.allow_taboo_push is set to False, those moves should not be
    included in the returned list of actions.

    If self.macro is set True, the 'actions' function should return
    macro actions. If self.macro is set False, the 'actions' function should
    return elementary actions.


    '''
    #
    #         "INSERT YOUR CODE HERE"
    #
    #     Revisit the sliding puzzle and the pancake puzzle for inspiration!
    #
    #     Note that you will need to add several functions to
    #     complete this class. For example, a 'result' function is needed
    #     to satisfy the interface of 'search.Problem'.


    def __init__(self, goal, warehouse):
        self.warehouse = warehouse
        self.initial = warehouse.worker
        self.goal = goal

    def actions(self, state):
        """
        Return the list of actions that can be executed in the given state.

        As specified in the header comment of this class, the attributes
        'self.allow_taboo_push' and 'self.macro' should be tested to determine
        what type of list of actions is to be returned.

        When self.allow_taboo_push is set to True, the 'actions' function should 
        return all possible legal moves including those that move a box on a taboo 
        cell. If self.allow_taboo_push is set to False, those moves should not be
        included in the returned list of actions.
    
        If self.macro is set True, the 'actions' function should return 
        macro actions. If self.macro is set False, the 'actions' function should 
        return elementary actions.
        """
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        directions_words = ['Left', 'Right', 'Up', 'Down']
        actions = []
        for id, direction in enumerate(directions):
            new_worker_x = state[0] + direction[0]
            new_worker_y = state[1] + direction[1]
            new_worker = (new_worker_x, new_worker_y)
            if new_worker in self.warehouse.walls:
                continue
            if new_worker in self.warehouse.boxes:
                continue
            actions.append(directions_words[id])
        return actions

    def result(self, state, action):
        '''
        @param state: a tuple of the worker and boxes
        @param action: a tuple of the action
        '''
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        directions_words = ['Left', 'Right', 'Up', 'Down']
        for wordId, direction_word in enumerate(directions_words):
            if action == direction_word:
                workerState_X = state[0] + directions[wordId][0]
                workerState_Y = state[1] + directions[wordId][1]
                new_workerState = (workerState_X, workerState_Y)
                return new_workerState
                    

    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal, as specified in the constructor. Override this
        method if checking against a single self.goal is not enough."""
        return state == self.goal

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def can_go_there(warehouse, dst):
    '''
    Determine whether the worker can walk to the cell dst=(row,column)
    without pushing any box.

    @param warehouse: a valid Warehouse object

    @return
      True if the worker can walk to cell dst=(row,column) without pushing any box
      False otherwise
    '''

    #checks if the action is valid
    dst = (dst[1], dst[0])
    problem = SokobanCanGoPuzzle(dst, warehouse)
    node = search.breadth_first_graph_search(problem)
    if node == None:
        return False
    else:
        warehouse.worker = problem.goal
        return True


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def solve_sokoban_macro(warehouse):
    '''
    Solve using macro actions the puzzle defined in the warehouse passed as
    a parameter. A sequence of macro actions should be
    represented by a list M of the form
            [ ((r1,c1), a1), ((r2,c2), a2), ..., ((rn,cn), an) ]
    For example M = [ ((3,4),'Left') , ((5,2),'Up'), ((12,4),'Down') ]
    means that the worker first goes the box at row 3 and column 4 and pushes it left,
    then goes to the box at row 5 and column 2 and pushes it up, and finally
    goes the box at row 12 and column 4 and pushes it down.

    @param warehouse: a valid Warehouse object

    @return
        If puzzle cannot be solved return the string 'Impossible'
        Otherwise return M a sequence of macro actions that solves the puzzle.
        If the puzzle is already in a goal state, simply return []
    '''
    
    problem = SokobanPuzzle(warehouse)
    problem.macro = True
    def h(node):
        boxes = node.state[1:]
        goals = warehouse.targets
        total = 0
        for box in boxes:
            shortest = 10000000
            for goal in goals:
                xdist = abs(box[0] - goal[0])
                ydist = abs(box[1] - goal[1])
                distance = xdist + ydist
                if shortest == None or distance < shortest:
                    shortest = distance
            total = total + shortest
        return total

    #node = search.depth_first_graph_search(problem)
    #node = search.breadth_first_graph_search(problem)
    node = search.astar_graph_search(problem, h)
    #node = search.uniform_cost_search(problem)
    #node = search.breadth_first_tree_search(problem)
        
   
    
    #node = search.breadth_first_graph_search(problem)
    if node == None:
        return ["Impossible"]
    return node.solution()










# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
