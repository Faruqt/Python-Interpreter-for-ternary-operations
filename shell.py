from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter
import shell

def run(sample, inpt):
	
    text = inpt + sample
    lexer = Lexer(text)
    tokens = lexer.generate_tokens()
    # print(list(tokens))
    parser = Parser(tokens)
    tree = parser.parse()
    # print(tree)
    interpreter = Interpreter()
    value = interpreter.visit(tree)
    print(value)
