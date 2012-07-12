def fuzz_checker(check_sudoku):
    sanity_check_the_checker(check_sudoku)
def sanity_check_the_checker(sudoku_checker):
    """ given `sudoku_checker` a sudoku checker function, attempts to ferret out common issues with checking
    for valid input.  Raises AssertionError s if the function fails to conform to expectations"""
    try:
        valid_row = range(1, 10)
        illegal = (0, [], range(10), [range(10), range(10), 0, range(10), 1, range(10), range(10), range(10), range(10)], [valid_row] * 8 + [range(2, 11)])
        invalid = ([[1]*9] * 9,) 
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
    except AssertionError:
        raise
    except Exception as e:
        print("Raised error type {etype} with msg {emsg}.".format(etype=type(e), emsg=str(e)))
        raise
    return True
