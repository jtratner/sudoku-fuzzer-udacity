# the following are from Goldsong on udacity
bad_subgrid = [[9,8,7,6,5,4,3,2,1],
        [8,7,6,5,4,3,2,1,9],
        [7,6,5,4,3,2,1,9,8],
        [6,5,4,3,2,1,9,8,7],
        [5,4,3,2,1,9,8,7,6],
        [4,3,2,1,9,8,7,6,5],
        [3,2,1,9,8,7,6,5,4],
        [2,1,9,8,7,6,5,4,3],
        [1,9,8,7,6,5,4,3,2]]

# floating point grid, from Goldsong
fpgd = [[2,9,0,0,0,0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9, 5.5, 0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]
# bool grid again from Goldsong. not included by default, because
# honestly it's not clear that it's wrong.
boolg = [[2,9,0,0, False, 0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9,5,0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]
# this one is also from Goldsong, not included by default
# totally dependent on whether you think that floating point numbers should be excluded or not
fpgd2 = [[2,9,0,0,0,0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9, 5., 0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]
def fuzz_checker(check_sudoku, check_edges):
    sanity_check_the_checker(check_sudoku, check_edges)
    return True
def sanity_check_the_checker(sudoku_checker, check_edges):
    """ given `sudoku_checker` a sudoku checker function, attempts to ferret out common issues with checking
    for valid input.  Raises AssertionError s if the function fails to conform to expectations"""
    try:
        valid_row = range(1, 10)
        illegal = [0, [], range(10), [valid_row, valid_row, 0, range(9), 1, range(9), range(9), valid_row, valid_row],
                [valid_row] * 8 + [[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]], fpgd]
        illegal.append([[0] * 9] * 8 + [set(range(9))])
        invalid = ([[1]*9] * 9, bad_subgrid) 
        edges = [fpgd2, boolg]
        for s in illegal:
            res = sudoku_checker(s) 
            assert res is None, "Failed to detect that {s} was illegal. Returned {res} instead of `None`".format(s=s, res=res)
        for s in invalid:
            res = sudoku_checker(s)
            assert res is False, "Failed to return False for invalid sudoku {s}. Returned {res} instead of `False`".format(s=s, res=res)
        base = [[0] * 9] * 9
        for i in range(9):
            s = base[:i]
            res = sudoku_checker(s)
            assert res is None, "Failed to detect that {s} was illegal. Returned {res} instead of `None`".format(s=s, res=res)
        if check_edges:
            for s in edges:
                res = sudoku_checker(s)
                assert res is None, "Checker failed to detect that {s} was illegal. Returned {res} instead of `None`".format(res=res, s=s)
    except AssertionError:
        raise
    except Exception as e:
        print("Raised error type {etype} with msg {emsg}.".format(etype=type(e), emsg=str(e)))
        raise
    return True
