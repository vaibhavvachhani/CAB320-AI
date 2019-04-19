import time
import mySokobanSolver

import time
import csv
from sokoban import Warehouse

if __name__ == "__main__":

    
    num = int(input("Warehouse Num: "))
    problem_file = "./warehouses/warehouse_{:02d}.txt".format(num)

    # Test marco solver
    
    wh = Warehouse()
    wh.load_warehouse(problem_file)
    print(wh)
    print("Macro Solver")
    t0 = time.time()
    result = mySokobanSolver.solve_sokoban_macro(wh)
    t1 = time.time()

    print('End time: {:.6f} seconds'.format(t1-t0))
    print("Solution: {0}".format(result))
    print("Solution Len: {0} \n".format(len(result)))
    
    
    # Test element solver
    
    wh = Warehouse()
    wh.load_warehouse(problem_file)
    print("Element Solver")
    t0 = time.time()
    result = mySokobanSolver.solve_sokoban_elem(wh)
    t1 = time.time()

    print('End time: {:.6f} seconds'.format(t1-t0))
    print("Solution: {0}".format(result))
    print("Solution Len: {0} \n".format(len(result)))
