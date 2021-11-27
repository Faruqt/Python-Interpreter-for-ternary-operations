from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter

sample="""if (var_1 == 2, 0, if (var_2 == 4, 15, 0) ) + if (var_2 == 3, 5, 0) - if (var_4 == 2, 0, 5) + if (var_3 == 3, 5, 0) """

while True:
    try:
        inpt = input("Enter variable as object:  ")
        text = inpt + sample
        lexer = Lexer(text)
        tokens = lexer.generate_tokens()
        # print(list(tokens))
        parser = Parser(tokens)
        tree = parser.parse()
        # print(tree)
        if not tree:continue
        interpreter = Interpreter()
        value = interpreter.visit(tree)
        print(value)
    except Exception as e:
        print(e)
    


#input example
# {var_1: 1, var_2: 4, var_3: 2, var_4: 3}
