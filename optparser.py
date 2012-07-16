import sys
import optparse

parser = optparse.OptionParser()
parser.add_option("-t", "--test", default="all", nargs=1,
        choices=["all", "checker", "solver"])

parser.add_option("-m", "--mutations", help="""set number of
        mutations for solver fuzzer""", default=20)
parser.add_option("--iters", help="""set number of
iterations for solver fuzzer""", default=10)
parser.add_option("--no-strict", help="disable strict checking (e.g. 5.0, True, False, etc)", action="store_false", dest="check_edges", default=True)
def get_args():
    options, args = parser.parse_args()
    if len(args) < 1:
        sys.exit("ERROR: must provide a file location for solver and checker")
    options_dict = dict(
            test = options.test,
            solver_file = args[0],
            check_edges = options.check_edges
            )
    for argname in ("mutations", "iters"):
        if hasattr(options, argname):
            options_dict[argname] = int(getattr(options, argname))
    return options_dict


