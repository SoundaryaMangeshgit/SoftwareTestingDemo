
import fuzzingbook.fuzzingbook.fuzzingbook_utils
from fuzzingbook.fuzzingbook.SymbolicFuzzer import AdvancedSymbolicFuzzer, SimpleSymbolicFuzzer
from inspect import getmembers, isfunction
import example
import inspect

def check_triangle(a: int, b: int, c: int) -> int:
    if a == b:
        if a == c:
            if b == c:
                return "Equilateral"
            else:
                return "Isosceles"
        else:
            return "Isosceles"
    else:
        if b != c:
            if a == c:
                return "Isosceles"
            else:
                return "Scalene"
        else:
            return "Isosceles"


def if_triangle(a: int, b: int, c: int) -> int:
    if a + b > c:
        return True
    if b + c > a:
        return True

    if c + a > b:
        return True
    else:
        return False


import z3
def get_annotations(fn):
    sig = inspect.signature(fn)
    return ([(i.name, i.annotation)
             for i in sig.parameters.values()], sig.return_annotation)
params, ret = get_annotations(if_triangle)
params, ret
SYM_VARS = {
    int: (
        z3.Int, z3.IntVal), float: (
            z3.Real, z3.RealVal), str: (
                z3.String, z3.StringVal)}
def get_symbolicparams(fn):
    params, ret = get_annotations(fn)
    return [SYM_VARS[typ][0](name)
            for name, typ in params], SYM_VARS[ret][0]('__return__')
(a, b, c), r = get_symbolicparams(if_triangle)
a, b, c, r

################################################################ FINDING SOLUTIONS FOR THE PATH
z3.solve(a>b, b>c, c>b) # no solution
z3.solve(a<b, b<c, c>a)
z3.solve(b>c, a>b, c<a)
################################################################################################
# Generate all possible paths from fnenter to all paths in the function.
symfz_ct = SimpleSymbolicFuzzer(if_triangle)
paths = symfz_ct.get_all_paths(symfz_ct.fnenter)
print(len(paths))

for i in range(0,len(paths)):
    print(paths[i])