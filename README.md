sudoku-fuzzer-udacity
=====================

Sudoku fuzzers for Udacity class CS258

If you have additional items to add to the fuzzer, please contribute 'em!

Running the fuzzer
------------------

To run, clone/download/whatever the repo, then run:

    python run_fuzzer.py path/to/my/solver_and_checker.py

And the program will attempt to fuzz your solver and checker.

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

Checker fuzzer - written by Jeffrey Tratner (+ inspired by fuzzer test cases from
Bill Barry and Brandon)

Tricky example of a fail-in-subgrid-only grid and a grid with floating point numbers from Goldsong

License
-------
Freely provided under the MIT License
