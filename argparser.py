import argparse

parser = argparse.ArgumentParser()
parser.add_argument("solver_file", metavar="file", help="""python file
containing solver and checker functions (as "check_sudoku" and
"solve_sudoku")""", nargs=1)
parser.add_argument("-t", "--test", choices=["checker",
    "solver", "all"], help = """Choose whether to test checker, solver or
    both (default is both)""", default="all")
parser.add_argument("-m", "--mutations", type=int, metavar="#", help="""set number of
        mutations for solver fuzzer""", dest="mutations", default=20)
parser.add_argument("--iters", type=int,  help="""set number of
iterations for solver fuzzer""", default=10)

def get_args():
    args = parser.parse_args()
    options_dict = dict(
            test = args.test,
            solver_file = args.solver_file[0])
    for argname in ("mutations", "iters"):
        if hasattr(args, argname):
            options_dict[argname] = getattr(args, argname)
    return options_dict

