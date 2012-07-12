def fuzz_it(check_sudoku=None, solve_sudoku=None, test="all", iters=10,
        mutations=10, check_edges=None):
    if test in ("all", "checker"):
        from fuzz_checker import fuzz_checker
        success = fuzz_checker(check_sudoku, check_edges)
        if not success:
            print "Failed fuzzing of sudoku checker"
            return
        else:
            print "Sudoku checker passed all tests!"
    if test in ("all", "solver"):
        from fuzz_solver import fuzz_solver
        success = fuzz_solver(check_sudoku, solve_sudoku, iters=iters,
                mutates=mutations)
        if not success:
            print "Failed fuzzing of sudoku solver"
            return
        else:
            print "Sudoku solver passed all tests!"

if __name__ == '__main__':
    try:
        from argparser import get_args
    except ImportError:
        try:
            from optparser import get_args
        except ImportError:
            print """couldn't import an option parser. Run in interactive mode."""
    args_dict = get_args()
    import imp, os
    filepath = os.path.abspath(args_dict["solver_file"])
    mod_name, file_ext = os.path.splitext(os.path.split(filepath)[-1])
    if file_ext.lower() == '.py':
        user_mod = imp.load_source(mod_name, filepath)
    elif file_ext.lower() == ".pyc":
        user_mod = imp.load_compiled(mod_name, filepath)
    del args_dict["solver_file"]
    try:
        args_dict["check_sudoku"] = user_mod.check_sudoku
    except AttributeError:
        raise AttributeError("Module `{mod}` has no function"
                "`check_sudoku`".format(mod=mod_name))
    if args_dict["test"] in ("all", "solver"):
        try:
            args_dict["solve_sudoku"] = user_mod.solve_sudoku
        except AttributeError:
            raise AttributeError("Module {mod} has no function"
                    "`solve_sudoku`".format(mod=mod_name))
    fuzz_it(**args_dict)

