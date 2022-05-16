[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=7564077&assignment_repo_type=AssignmentRepo)
# tests
Write valid input files for the NFA and DFA modules that you implemented.
Respect the folder structure provided in the templte. Write 3 DFA config files and 3 NFA confing files.
Two of each should be made accordingly to the specifications below. For one of each you're free to implement any automaton. Provide a description of what your automatons should accept in a file `MY_AUTOMATON.MD` in your root directory.

## Test structure
Every test directory contains:
- a `.cfg` file
- `.in` files
- `.out` files

`automaton.cfg` contains the config of the automaton you have to specify

`string_{no_test}.in` contains a string that will be consumed by the automaton you speciffied in the `automaton.cfg` file in the same directory

`string_{no_test}.out` contains `1` if the automaton should accept the string, 0 otherwise

For every config file, write 5 tests that should be accepted and 5 tests that should be rejected. 
## Clock - tests1
One test for NFA and one for DFA should be the following: 
A one config file for an automaton that accepts time specifications of a digital clock with 24 hours or analog clock with 12 hours. 

The following examples should be accepted:
- 4 p m (special case only for the analog clock)
- 7 : 3 8 p m
- 2 3 : 4 2
- 3 : 1 6 
- 3 : 1 6 a m
- 1 3 : 0 3
- 3 : 0 3 p m
- 0 : 0 1


Not accepted:
- 0 3 : 0 3
- 1 3
- 0 3 A M
- 0 3 : 4 3
- 1 3 : 4
- 3 : 4 P M
- 0 0 : 0 0
- 0 0 : 0 0 A M

## Binary number divisible with 7 - tests2
Another test for NFA and one for DFA should be the following: 
A one config file for an automaton that accepts binary numbers divisible by 7. 

The following examples should be accepted:
- 0
- 1 1 1
- 1 1 1 0
- 1 0 1 1 0 0 0 0 1 1

Not accepted:
- 0 0
- 0 1 1 1
- 1 1 0

## Arbitrary automaton - tests3
Come up with an adversarial config and tests for your colleagues - think of special cases they missed when validating the DFA and NFA. 

Write a file `MY_AUTOMATON.MD` in the root directory in which you describe what the automaton is supposed to accept and reject.

Do NOT implement weird config files such that their automatons would spit a validation error, if more than half your colleagues get a validation error, then your config will be considered invalid.

# How your programs will be run:

1. `dfa.py automaton.cfg "w1 w2 w3 w4 w5"` (w1 w2 w3 w4 w5 are from string_{no_test})

2. `nfa.py automaton.cfg implementation_1 "w1 w2 w3 w4 w5"`

3. `nfa.py automaton.cfg "w1 w2 w3 w4 w5"`

# Important: modification of previous programs 
#### Why you will get two extra weeks for the labs
Modify your current projects (DFA and NFA) to output `accept(ed)` for accepted strings, `reject(ed)` for rejected strings, and `invalid` for invalid config files.

# Notes
For Python3 implementations, a test similar with `tester.py` can be used to eveluate your work (you don't have to write the tester). For NFA, select a default implementation in your code such that it's abstracted away so it runs as in example `3.` (use your favorite implementation as the default one). This will bring you 0.25 bonus points. Write in the Google Sheets, 'Studenți' page wether you preffer this way of testing.
