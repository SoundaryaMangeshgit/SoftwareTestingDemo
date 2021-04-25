from fuzzingbook.SymbolicFuzzer import AdvancedSymbolicFuzzer, SimpleSymbolicFuzzer
from inspect import getmembers, isfunction
import example
import re

for func in getmembers(example, isfunction):

    asymfz_gcd = AdvancedSymbolicFuzzer(func[1], max_iter=10, max_tries=10, max_depth=10)
    paths = asymfz_gcd.get_all_paths(asymfz_gcd.fnenter)

    print("------------------------------------------------------------")
    print("Function:",func[0],". Found total paths: ", len(paths))

    print("\n")


    for i in range(len(paths)):

        print("------------------------------")
        print("Path#", i)
        x = str(paths[i].get_path_to_root())
        check_return = x.find('return')
        pattern = "line(.*?)return"
        substring = re.search(pattern, x)
        if (substring != None):
            substring = re.search(pattern, x).group((1))
            index = substring.rfind('line')
            extract_str = substring[index:index + 8]
            print("The line number:", extract_str)
        else:
            print("NO SOLUTION FOUND")
        print("Constraints:", asymfz_gcd.extract_constraints(paths[i].get_path_to_root()))
        print("Solution:", asymfz_gcd.solve_path_constraint(paths[i].get_path_to_root()))