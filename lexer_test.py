import unittest
from tokens import Token, TokenType
from lexer import Lexer

class TestLexer(unittest.TestCase):

	def test_empty(self):
		tokens = list(Lexer("").generate_tokens())
		self.assertEqual(tokens, [])
	
	def test_whitespace(self):
		tokens = list(Lexer(" \t\n  \t\t\n\n").generate_tokens())
		self.assertEqual(tokens, [])

	def test_numbers(self):
		tokens = list(Lexer("123 ").generate_tokens())
		self.assertEqual(tokens, [
			Token(TokenType.NUMBER, 123.000),
		])

	def test_operators(self):
		tokens = list(Lexer("+-*/").generate_tokens())
		self.assertEqual(tokens, [
			Token(TokenType.PLUS),
			Token(TokenType.MINUS),
			Token(TokenType.MULTIPLY),
			Token(TokenType.DIVIDE),
		])

	def test_parens(self):
		tokens = list(Lexer("()").generate_tokens())
		self.assertEqual(tokens, [
			Token(TokenType.LPAREN),
			Token(TokenType.RPAREN),
		])

	def test_obj(self):
		tokens = list(Lexer("{}").generate_tokens())
		self.assertEqual(tokens, [
			Token(TokenType.INPUTSTART),
			Token(TokenType.INPUTEND),
		])

	def test_conditions(self):
		tokens = list(Lexer("var_2 == 3").generate_tokens())
		self.assertEqual(tokens, [
			Token(TokenType.VARIABLE, 'var_2'),
			Token(TokenType.EQUALTO),
			Token(TokenType.NUMBER, 3),
		])

	def test_ternary(self):
		tokens = list(Lexer("if (var_2 == 3, 5, 0)").generate_tokens())
		self.assertEqual(tokens, [
			Token(TokenType.STATEMENT),
			Token(TokenType.LPAREN),
			Token(TokenType.VARIABLE, 'var_2'),
			Token(TokenType.EQUALTO),
			Token(TokenType.NUMBER, 3),
			Token(TokenType.TRUTHY),
			Token(TokenType.NUMBER, 5),
			Token(TokenType.FALSY),
			Token(TokenType.NUMBER, 0),
			Token(TokenType.RPAREN),
		])

	def test_embedded_truthy_ternary(self):
		tokens = list(Lexer("if (var_2 == 3, if (var_3 == 2, 4, 6) ,5)").generate_tokens())
		self.assertEqual(tokens, [
			Token(TokenType.STATEMENT),
			Token(TokenType.LPAREN),
			Token(TokenType.VARIABLE, 'var_2'),
			Token(TokenType.EQUALTO),
			Token(TokenType.NUMBER, 3),
			Token(TokenType.TRUTHY),
			Token(TokenType.STATEMENT),
			Token(TokenType.LPAREN),
			Token(TokenType.VARIABLE, 'var_3'),
			Token(TokenType.EQUALTO),
			Token(TokenType.NUMBER, 2),
			Token(TokenType.TRUTHY),
			Token(TokenType.NUMBER, 4),
			Token(TokenType.FALSY),
			Token(TokenType.NUMBER, 6),
			Token(TokenType.RPAREN),
			Token(TokenType.FALSY),
			Token(TokenType.NUMBER, 5),
			Token(TokenType.RPAREN),
		])
		
	def test_embedded_falsy_ternary(self):
		tokens = list(Lexer("if (var_2 == 3, 5, if (var_3 == 2, 4, 6))").generate_tokens())
		self.assertEqual(tokens, [
			Token(TokenType.STATEMENT),
			Token(TokenType.LPAREN),
			Token(TokenType.VARIABLE, 'var_2'),
			Token(TokenType.EQUALTO),
			Token(TokenType.NUMBER, 3),
			Token(TokenType.TRUTHY),
			Token(TokenType.NUMBER, 5),
			Token(TokenType.FALSY),
			Token(TokenType.STATEMENT),
			Token(TokenType.LPAREN),
			Token(TokenType.VARIABLE, 'var_3'),
			Token(TokenType.EQUALTO),
			Token(TokenType.NUMBER, 2),
			Token(TokenType.TRUTHY),
			Token(TokenType.NUMBER, 4),
			Token(TokenType.FALSY),
			Token(TokenType.NUMBER, 6),
			Token(TokenType.RPAREN),
			Token(TokenType.RPAREN),
		])
	def test_all(self):
		tokens = list(Lexer("if (var_1 == 2, 0, if (var_2 == 4, 15, 0) ) + if (var_2 == 3, 5, 0) - if (var_4 == 2, 0, 5) + if (var_3 == 3, 5, 0) ").generate_tokens())
		self.assertEqual(tokens, [
			Token(TokenType.STATEMENT),
			Token(TokenType.LPAREN),
			Token(TokenType.VARIABLE, 'var_1'),
			Token(TokenType.EQUALTO),
			Token(TokenType.NUMBER, 2),
			Token(TokenType.TRUTHY),
			Token(TokenType.NUMBER, 0),
			Token(TokenType.FALSY),
			Token(TokenType.STATEMENT),
			Token(TokenType.LPAREN),
			Token(TokenType.VARIABLE, 'var_2'),
			Token(TokenType.EQUALTO),
			Token(TokenType.NUMBER, 4),
			Token(TokenType.TRUTHY),
			Token(TokenType.NUMBER, 15),
			Token(TokenType.FALSY),
			Token(TokenType.NUMBER, 0),
			Token(TokenType.RPAREN),
			Token(TokenType.RPAREN),
			Token(TokenType.PLUS),
			Token(TokenType.STATEMENT),
			Token(TokenType.LPAREN),
			Token(TokenType.VARIABLE, 'var_2'),
			Token(TokenType.EQUALTO),
			Token(TokenType.NUMBER, 3),
			Token(TokenType.TRUTHY),
			Token(TokenType.NUMBER, 5),
			Token(TokenType.FALSY),
			Token(TokenType.NUMBER, 0),
			Token(TokenType.RPAREN),
			Token(TokenType.MINUS),
			Token(TokenType.STATEMENT),
			Token(TokenType.LPAREN),
			Token(TokenType.VARIABLE, 'var_4'),
			Token(TokenType.EQUALTO),
			Token(TokenType.NUMBER, 2),
			Token(TokenType.TRUTHY),
			Token(TokenType.NUMBER, 0),
			Token(TokenType.FALSY),
			Token(TokenType.NUMBER, 5),
			Token(TokenType.RPAREN),
			Token(TokenType.PLUS),
			Token(TokenType.STATEMENT),
			Token(TokenType.LPAREN),
			Token(TokenType.VARIABLE, 'var_3'),
			Token(TokenType.EQUALTO),
			Token(TokenType.NUMBER, 3),
			Token(TokenType.TRUTHY),
			Token(TokenType.NUMBER, 5),
			Token(TokenType.FALSY),
			Token(TokenType.NUMBER, 0),
			Token(TokenType.RPAREN),
		])
