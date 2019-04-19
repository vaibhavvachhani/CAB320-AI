import time
import csv
from sokoban import Warehouse
from mySokobanSolver import *

FIRST_WAREHOUSE = 1
LAST_WAREHOUSE = 200


def print_taboo_spaces(warehouse_id):
    """
    Calculates the taboo cells for the given warehouse id and prints them
    @param warehouse_id: ID of warehouse to load taboo spaces for
    """
    problem_file = "./warehouses/warehouse_{:02d}.txt".format(warehouse_id)
    wh = Warehouse()
    wh.load_warehouse(problem_file)
    print(wh)
    print("TABOO CELLS: ")
    taboo = taboo_cells(wh)
    print(taboo)


if __name__ == "__main__":
    for warehouse_number in range(FIRST_WAREHOUSE, LAST_WAREHOUSE, 2):
        print("Testing warehouse {:02d}".format(warehouse_number))
        print_taboo_spaces(warehouse_number)
