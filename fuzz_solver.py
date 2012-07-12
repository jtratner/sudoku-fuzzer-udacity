# Use a different solved board to generate different tests.
valid = [[5,3,4,6,7,8,9,1,2],
         [6,7,2,1,9,5,3,4,8],
         [1,9,8,3,4,2,5,6,7],
         [8,5,9,7,6,1,4,2,3],
         [4,2,6,8,5,3,7,9,1],
         [7,1,3,9,2,4,8,5,6],
         [9,6,1,5,3,7,2,8,4],
         [2,8,7,4,1,9,6,3,5],
         [3,4,5,2,8,6,1,7,9]]

# test cases with no solution
no_soln1 = [
[1,2,3,4,5,6,7,8,0],
[0,0,0,0,0,0,0,0,9],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0]]

no_soln2 = [
[1, 2, 3, 0, 0, 0, 0, 0, 0],
[4, 5, 0, 0, 0, 0, 6, 0, 0],
[0, 0, 0, 6, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0]]
import random

# Make a copy of a grid so we can modify it without touching the original
def copy (grid):
    return map (lambda x: x[:], grid)

# Assert than a solution remains solvable after mutates-many moves are undone.
# Run iters-many tests of this nature.
def fuzz_solution(soln, mutates, iters, check_sudoku, solve_sudoku):
    """ fuzzes a given *valid* solution """
    random.seed()
    for i in range(iters):
        board = copy(soln)
        # Undo a set of moves. This should leave the board solvable
        for mutate in range(mutates):
            x = random.randrange(0,9)
            y = random.randrange(0,9)
            # Might already be 0 in which case we didn't undo "mutates" moves
            # but still generated a reasonable test case
            board[x][y] = 0
        # If this board is invalid the test harness screwed up
        assert check_sudoku(board), "Input checker failed with input {board}".format(board=board)
        # If it's unsolvable the solver screwed up
        assert solve_sudoku(board), "Solver failed to solve board {board}".format(board=board)
    return True

def check_no_valid_solns(solve_sudoku, tests=None):
    """ runs solver against cases with no solution"""
    tests = tests or [no_soln1, no_soln2]
    for test in tests:
        res = solve_sudoku(test)
        assert res is False, """Solver failed to return False for valid, but unsolveable sudoku. 
Returned {res} instead. Input was: {test}""".format(test=test, res=res)
    return True

def fuzz_solver(check_sudoku, solve_sudoku, mutates=10, iters=10, soln=None, tests=None):
    soln = soln or valid
    return check_no_valid_solns(solve_sudoku, tests) and fuzz_solution(valid, mutates, iters, check_sudoku, solve_sudoku)
