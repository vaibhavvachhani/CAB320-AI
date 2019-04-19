import time
import mySokobanSolver

import time
import csv
from sokoban import Warehouse

if __name__ == "__main__":
    num = int(input("Warehouse Num: "))
    problem_file = "./warehouses/warehouse_{:02d}.txt".format(num)
    
    wh = Warehouse()
    wh.load_warehouse(problem_file)

    start_time = time.process_time()
    result = mySokobanSolver.solve_sokoban_macro(wh)
    end_time = time.process_time()

    print("Macro Solver")
    print("End Time: " + str(end_time - start_time))
    print("Solution: " + str(result))
    print("Solution Len: " + str(len(result)))
    
    wh = Warehouse()
    wh.load_warehouse(problem_file)

    start_time = time.process_time()
    result = mySokobanSolver.solve_sokoban_elem(wh)
    end_time = time.process_time()

    print("Elem Solver")
    print("End Time: " + str(end_time - start_time))
    print("Solution: " + str(result))
    print("Solution Len: " + str(len(result)))
