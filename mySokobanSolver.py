
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

#global variable
taboo_cells_list = []

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
    left = (x-1, y)
    right = (x+1, y)
    top = (x, y-1)
    down = x, y+1)
    example x,y = (2,2)
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
    ##         "INSERT YOUR CODE HERE"
    walls = warehouse.walls
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
    for i in range(len(walkable_coords)):
        number_of_walls = number_of_walls_surrounded(walls, walkable_coords[i])
        if number_of_walls > 2:
            taboo_coords.append(walkable_coords[i])
        elif number_of_walls == 2:
            walls_around_list = walls_around(walls, walkable_coords[i])
            if walls_around_list[0][0] != walls_around_list[1][0] and walls_around_list[0][1] != walls_around_list[1][1]:
                taboo_coords.append(walkable_coords[i])

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

    # by default does not allow push of boxes on taboo cells
    allow_taboo_push = False

    # use elementary actions if self.macro == False
    macro = False

    def __init__(self, warehouse):
        self.initial = warehouse.worker
        self.goal = warehouse.targets
        self.warehouse = warehouse

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
        list_of_movements = [(state[0]-1, state[1]), (state[0]+1, state[1]), (state[0], state[1]-1), (state[0], state[1]+1)]
        for wall in range(len(self.warehouse.walls)):
            thisWall = self.warehouse.walls[wall]
            if thisWall in list_of_movements:
                list_of_movements.remove(thisWall)

        if self.allow_taboo_push == False:
            for cell in range(len(taboo_cells_list)):
                this_cell = taboo_cells_list[cell]
                if this_cell in list_of_movements:
                    list_of_movements.remove(this_cell)

        if self.macro:
            for move in range(len(list_of_movements)):
                movement = list_of_movements[move]
                if movement not in self.warehouse.boxes:
                    list_of_movements.remove(movement)
        return list_of_movements

    def result(self, state, action):
        return None
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

    ##         "INSERT YOUR CODE HERE"
    # boxes

    for action in range(len(action_seq)):
        if action_seq[action] == 'Left':
            warehouse.worker = (warehouse.worker[0] - 1, warehouse.worker[1])
            last_action = 'Left'
        elif action_seq[action] == 'Right':
            warehouse.worker = (warehouse.worker[0] + 1, warehouse.worker[1])
            last_action = 'Right'
        elif action_seq[action] == 'Up':
            warehouse.worker = (warehouse.worker[0], warehouse.worker[1] - 1)
            last_action = 'Up'
        elif action_seq[action] == 'Down':
            warehouse.worker = (warehouse.worker[0], warehouse.worker[1] + 1)
            last_action = 'Down'

        #boxes
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
        if warehouse.worker in warehouse.walls:
            return "Failure"

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

    ##         "INSERT YOUR CODE HERE"
    elements = []
    boxes = warehouse.boxes
    worker = warehouse.worker
    walls = warehouse.walls
    targets = warehouse.targets
    not_in_box = True
    for target in range(len(targets)):
        if targets[target] not in boxes:
            not_in_box = False
    if not_in_box == True:
        return elements
    problem = SokobanPuzzle(warehouse)
    queue = search.PriorityQueue()
    print(search.tree_search(problem, queue))
    print(problem.goal)
    return elements

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

    ##         "INSERT YOUR CODE HERE"
    #raise NotImplementedError()

    canmove = True

    col, row = warehouse.worker
    print(warehouse)
    for box in warehouse.boxes:

        while ((row, col) != dst):

            if (dst[0] < row):
                row = row - 1
            elif (dst[0] > row):
                row = row + 1

            if (dst[1] < col):
                col = col - 1
            elif (dst[1] > col):
                col = col + 1

            print("worker", (row , col))
            print("box", box)
            print("dst" , dst)
            print("\n")


            if (box[1] == row) & (box[0] == col):
                return False
            else:
                canmove = True
        return canmove

    print(dst)


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

    ##         "INSERT YOUR CODE HERE"

    #raise NotImplementedError()

    print(warehouse)

    output = []
    wcol, wrow = warehouse.worker

    for bcol, brow in warehouse.boxes:
        for tcol, trow in warehouse.targets:
            while((brow, bcol) != (trow, tcol)):

                if wrow < brow:
                    marco = 'Down'
                    wrow = brow
                    wcol = bcol
                    brow += 1

                elif wrow > brow:
                    marco = 'Up'
                    wrow = brow
                    wcol = bcol
                    brow -= 1

                if wcol < bcol:
                    marco = 'Right'
                    wrow = brow
                    wcol = bcol
                    bcol += 1
                elif wcol > bcol:
                    marco = 'Left'
                    wrow = brow
                    wcol = bcol
                    bcol -= 1

                print("worker", (wrow, wcol))
                print("box", (brow, bcol))
                print("targets", (trow, tcol))

                worker = ((wrow, wcol), marco)
                output.append(worker)

    return output










# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
