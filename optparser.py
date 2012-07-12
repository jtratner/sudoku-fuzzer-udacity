import sys
import optparse

parser = optparse.OptionParser()
parser.add_option("-t", "--test", default="all", nargs=1,
        choices=["all", "checker", "solver"])

def get_args():
    options, args = parser.parse_args()
    if len(args) < 1:
        sys.exit("ERROR: must provide a file location for solver and checker")
    options_dict = dict(
            test = options.test,
            solver_file = args[0],
            )
    return options_dict

