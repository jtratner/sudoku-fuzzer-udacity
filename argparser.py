import argparse

parser = argparse.ArgumentParser()
parser.add_argument("solver_file", metavar="file", help="""python file
containing solver and checker functions (as "check_sudoku" and
"solve_sudoku")""", nargs=1)
parser.add_argument("-t", "--test", choices=["checker",
    "solver", "all"], help = """Choose whether to test checker, solver or
    both (default is both)""", default="all")

def get_args():
    args = parser.parse_args()
    return dict(
            test = args.test,
            solver_file = args.solver_file)

