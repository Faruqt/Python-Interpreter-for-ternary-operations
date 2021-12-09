# Python-Interpreter-for-ternary-operations

This interpreter takes input in the form of objects, tokenizes the input and samples, parses them and then interepretes them.

## Lexer

The lexer groups the input characters into small segments called tokens and identifies the type of each token.

The characters in the input `{var_1: 1, var_2: 4, var_3: 2, var_4: 3}` are grouped into the tokens: `INPUTSTART`, `VARIABLE:var_1`, `ISASSIGNED`, `NUMBER:1`, `VARIABLE:var_2`, `ISASSIGNED`, `NUMBER:4`}, {`VARIABLE:var_3`, `ISASSIGNED`, `NUMBER:2` and `VARIABLE:var_4`, `ISASSIGNED`, `NUMBER:3`, `INPUTEND`.

The characters in the sample `if (var_1 == 2, if (var_2 == 4, 15, 0), 0 )` are grouped into the tokens `STATEMENT` `LPAREN` `VARIABLE:var_1`, `EQUALTO`, `NUMBER:2`, `TRUTHY` , {`STATEMENT` `LPAREN` `VARIABLE:var_2`, `EQUALTO`, `NUMBER:4`, `TRUTHY`, `NUMBER:15` `FALSY`, `NUMBER:0` `RPAREN`, `FALSY`, `NUMBER:0`, `RPAREN`.

Whitespace is usually ignored by the lexer.

The tokens are then passed on to the parser.

## Parser

The created tokens are convereted into a logic tree by the parser, and then passed  to the interpreter.

## Interpreter

The interpeter executes the logic tree by carrying out all the logical and arithmetic operations and provides a result.

# Running the Program

Requirements:
 - [Python3](https://www.python.org/downloads/) ^3.8

Run: `$PYTHON3 main.py` and supply your input variables as a dictionary e.g `{var_1: 1, var_2: 4, var_3: 2, var_4: 3}`. 

Ensure your variable names match the variable names in the sample declared in `main.py`

Unit testing:
 - `$PYTHON3 -m unittest lexer_test parser_test interpreter_test`
