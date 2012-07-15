sudoku-fuzzer-udacity
=====================

Sudoku fuzzers for Udacity class CS258

If you have additional items to add to the fuzzer, please contribute 'em!

Running the fuzzer
------------------

To run, clone/download/whatever the repo, then run:

    python run_fuzzer.py path/to/my/solver_and_checker.py

And the program will attempt to fuzz your solver and checker.

Command line options:

1. --test | lets you choose which tests to run (checker, solver, or both)
2. --no-strict | doesn't run tests checking for False/floating point
3. --mutations | set number of mutations (number of little changes to make) for checker fuzzer
4. --iters | set number of iterations for fuzz_solver (basically, just impacts the amount of time)

Compatibility
-------------

Should be compatible with Python 2.5+ and Python 3, though I haven't tested it
on Python 3 yet.

Problems?
---------

Send me [an email](mailto:jeffrey.tratner@gmail.com) if you encounter any
problems.

Credits
-------

Original solution mutator -- by Brandon on Udacity.

Test runner, checker fuzzer and some no-solution sudoku - written by Jeffrey Tratner (+ inspired by fuzzer test cases from
Bill Barry and Brandon)

Great refactoring + random testers contributed by Kedar Bellare (Generation-based and Transformation-based)

Tricky example of a fail-in-subgrid-only grid and a grid with floating point numbers from Goldsong

License
-------
Freely provided under the MIT License

