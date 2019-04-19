
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
if __name__ == "__main__":

    def tester(num):
        problem_file = "./warehouses/warehouse_{:02d}.txt".format(num)

        wh = Warehouse()
        wh.load_warehouse(problem_file)

        t0 = time.time()    
        result = solve_sokoban_elem(wh)
        t1 = time.time()
        print ('Warehouse number:{0}'.format(num))
        print ('Uniform Solver elem took {:.6f} seconds'.format(t1-t0))

        wh = Warehouse()
        wh.load_warehouse(problem_file)

        t0 = time.time()    
        result = solve_sokoban_elem(wh)
        t1 = time.time()
        print ('Uniform Solver marco took {:.6f} seconds\n'.format(t1-t0))


    for num in [1, 3, 5, 9, 11, 15]:
        tester(num)

    for num in range(15, 100, 2):
        tester(num)

        

        

