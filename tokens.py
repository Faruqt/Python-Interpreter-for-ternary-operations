from enum import Enum
from dataclasses import dataclass


class TokenType(Enum):  # declaring the types of token and assigning an ID
    NUMBER = 0
    PLUS = 1
    MINUS = 2
    MULTIPLY = 3
    DIVIDE = 4
    LPAREN = 5  # left  parenthesis
    RPAREN = 6  # right parenthesis
    EQUALTO = 7
    NEQUALTO = 8
    LTHAN = 9
    GTHAN = 10
    GTEQ = 11
    LTEQ = 12
    STATEMENT = 13
    TRUTHY = 14
    FALSY = 15
    IS_ASSIGNED = 16
    VARIABLE = 17
    INPUT_COMPARE = 18  
    INPUTSTART =19  # could be array or object start
    INPUTEND =20    # could be array or object end


@dataclass
class Token:
    type: TokenType
    value: any = None

    def __repr__(self):
        # declaring format for string representation of the object
        return self.type.name + (f":{self.value}"
                                 if self.value is not None else "")
        # token type is returned and value is only returned if a value exists
