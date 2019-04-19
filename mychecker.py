
'''

Sanity check script to test your submission 'mySokobanSolver.py'


A similar script (with different inputs) will be used for marking your code.

Make sure that your code runs without errors with this script.


'''


from sokoban import Warehouse

from mySokobanSolver import my_team, taboo_cells, SokobanPuzzle, check_action_seq
from mySokobanSolver import solve_sokoban_elem, can_go_there, solve_sokoban_macro 

#from fredSokobanSolver import my_team, taboo_cells, SokobanPuzzle, check_action_seq
#from fredSokobanSolver import solve_sokoban_elem, can_go_there, solve_sokoban_macro 


import time
t0 = time.time()    
wh = Warehouse()
wh.load_warehouse("./warehouses/warehouse_11.txt")
answer = solve_sokoban_elem(wh)
t1 = time.time()
print(wh)
print(answer)
print ('A* Solver took {:.6f} seconds\n'.format(t1-t0))

        

