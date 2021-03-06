from fuzzingbook.SymbolicFuzzer import AdvancedSymbolicFuzzer, SimpleSymbolicFuzzer
from inspect import getmembers, isfunction
import importlib
import argparse

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

# Initiate the parser
parser = argparse.ArgumentParser()

# Add long and short argument
parser.add_argument("--file", "-f", nargs="?", const="example", default="example",  help="file to parse")
parser.add_argument("--iter_max", "-i", nargs="?", const=10, default=10,  help="set maximum iterations")
parser.add_argument("--tries_max", "-t", nargs="?", const=10, default=10, help="set maximum tries")
parser.add_argument("--depth_max", "-d", nargs="?", const=10, default=10, help="set maximum depth")

# Read arguments from the command line
args = parser.parse_args()

# Check for args
if args.iter_max:
    print("File: %s" % args.file)

if args.iter_max:
    print("Set maximum iterations to %s" % args.iter_max)

if args.tries_max:
    print("Set maximum tries to %s" % args.tries_max)

if args.depth_max:
    print("Set maximum depth to %s" % args.depth_max)

# The file gets executed upon import, as expected.
mymodule = importlib.import_module(args.file)

for func in getmembers(mymodule, isfunction):

    asymfz_gcd = AdvancedSymbolicFuzzer(func[1],
                                        max_iter=int(args.iter_max),
                                        max_tries=int(args.tries_max),
                                        max_depth=int(args.depth_max))

    paths = asymfz_gcd.get_all_paths(asymfz_gcd.fnenter)

    print("------------------------------------------------------------")
    print("Function:",func[0],". Found total paths: ", len(paths))

    for i in range(len(paths)):
        get_out = str(paths[i].get_path_to_root())
        positions = list(find_all(get_out, 'line['))
        lines = ''
        for k,j in enumerate(positions):
            if k:
                lines += ', '
            lines += get_out[j+5:get_out.find(']',j+5)] # 5 for 'line['
        print("------------------------------")
        print("Path#", i)
        print("Constraints:", asymfz_gcd.extract_constraints(paths[i].get_path_to_root()))
        print("Located at lines:", lines)
        print("Solution:", asymfz_gcd.solve_path_constraint(paths[i].get_path_to_root()))
