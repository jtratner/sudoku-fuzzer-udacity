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
import random, time

squares = [(i,j) for i in range(9) for j in range(9)]
units = dict(((i,j), [[(i,k) for k in range(9)]] + 
              [[(k,j) for k in range(9)]] + 
              [[(k,l) for k in range(i/3*3, i/3*3+3) for l in range(j/3*3, j/3*3+3)]]) 
             for (i,j) in squares)
peers = dict((s, set(sum(units[s], [])) - set([s]))
             for s in squares)

def erase(board, i, j, d):
    if d not in board[i][j]:
        return board
    board[i][j] = board[i][j].replace(d, '')
    if len(board[i][j]) == 0:
        return False # contradiction
    elif len(board[i][j]) == 1:
        d2 = board[i][j]
        if not all(erase(board, i1, j1, d2) for (i1, j1) in peers[i,j]):
            return False
    for unit in units[i,j]:
        numplaces = [(i1, j1) for (i1, j1) in unit if d in board[i1][j1]]
        if len(numplaces) == 0:
            return False
        elif len(numplaces) == 1:
            if not assign(board, numplaces[0][0], numplaces[0][1], d):
                return False
    return board

def assign(board, i, j, d):
    if all(erase(board, i, j, d2) for d2 in board[i][j].replace(d, '')):
        return board
    else:
        return False

def random_sudoku(N = 30):
    board = [['123456789' for _ in range(9)] for _ in range(9)]
    cells = [s for s in squares]
    random.shuffle(cells)
    for cell in cells:
        i,j = cell
        if not assign(board, i, j, random.choice(board[i][j])):
            break
        ds = [board[i][j] for i in range(9) for j in range(9) if len(board[i][j]) == 1]
        if len(ds) >= N and len(set(ds)) >= 8:
            return [map(lambda v: int(v) if len(v) == 1 else 0, row) for row in board]
    return random_sudoku(N)

def check_random_solns(solve_sudoku, check_sudoku, mutates, iters):
    random.seed()
    solved = 0
    fraction = 0.9
    for i in range(iters):
        # Generate a valid random board
        board = random_sudoku(mutates)
        bd = ''.join(''.join(map(lambda n: str(n), row)) for row in board)
        # If it's unsolvable the solver screwed up
        start = time.clock()
        soln = solve_sudoku(board)
        if soln is not None and soln is not False:
            solved += 1
        t = time.clock() - start
        if t > 5.0: 
            print "board[%d] %s took (%.2f seconds)" % (i, bd, t)
    assert solved > (fraction * iters), "Your solver failed on more than %.1f%% of random boards!" % (100*fraction)
    print "Your solver completed %d / %d random boards! Congrats!" % (solved, iters)
    return True        

# Random strategy 2: Take a valid board and perform transformations
# that do not change validity

# Transposing a grid maintains validity
def transpose(grid):
    return map(list, zip(*grid))

# Permutes the row/column with another row/column in the same range
# (i.e. 6 with 6-8, 0 with 0-2, etc.)
def permute(grid, i, row=True):
    if not row: grid = map(list, zip(*grid))
    j = random.choice(range(i/3*3, i/3*3+3))
    grid[j], grid[i] = grid[i], grid[j]
    return grid if row else transpose(grid)

# Permutes the row/column blocks (i.e. 0-2 with 6-8)
def permute_block(grid, i, row=True):
    if not row: grid = map(list, zip(*grid))
    bi = i*3
    bj = random.choice(range(3))*3
    for offset in range(3):
        grid[bi+offset], grid[bj+offset] = grid[bj+offset], grid[bi+offset]
    return grid if row else transpose(grid)

# Reflects the board along the horizontal or vertical axis
def reflect(grid, horizontal=True):
    if not horizontal: grid = map(list, zip(*grid))
    for i in range(9): grid[i].reverse()
    return grid if horizontal else transpose(grid)

def random_mutation_sudoku(soln, iters=1000):
    # generate a valid grid
    grid = copy(soln)
    choices = [['reflect', horizontal] for horizontal in (True, False)] + [['transpose']] + [['permute', i, row] for row in (True, False) for i in range(9)] + [['permute_block', bi, row] for row in (True, False) for bi in range(3)]
    for i in range(iters):
        choice = random.choice(choices)
        if choice[0] == 'reflect': grid = reflect(grid, *choice[1:])
        if choice[0] == 'transpose': grid = transpose(grid)
        if choice[0] == 'permute': grid = permute(grid, *choice[1:])
        if choice[0] == 'permute_block': grid = permute_block(grid, *choice[1:])
    return grid

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
    success = check_no_valid_solns(solve_sudoku, tests) and fuzz_solution(soln, mutates, iters, check_sudoku, solve_sudoku) and check_random_solns(solve_sudoku, check_sudoku, mutates, iters)
    if success and all(fuzz_solution(random_mutation_sudoku(soln), mutates, 1, check_sudoku, solve_sudoku) for _ in range(iters)):
        print "Your solver completed %d randomly generated boards with %d mutations! Congrats!" % (iters, mutates)
        return True
    else:
        return False
