import unittest
from tokens import Token, TokenType
from parser_ import Parser
from node import *

class TestParser(unittest.TestCase):

	def test_empty(self):
		tokens = []
		node = Parser(tokens).parse()
		self.assertEqual(node, None)

	def test_condit(self):
		tokens = [
			Token(TokenType.STATEMENT),
			Token(TokenType.LPAREN),
			Token(TokenType.VARIABLE, 'var_3'),
			Token(TokenType.EQUALTO),
			Token(TokenType.NUMBER,3),
			Token(TokenType.TRUTHY),
			Token(TokenType.NUMBER,4),
			Token(TokenType.FALSY),
			Token(TokenType.NUMBER,5),
			Token(TokenType.RPAREN),
		]
		node = Parser(tokens).parse()
		self.assertEqual(node, ComparisonNode(NumberNode(4), NumberNode(3), NumberNode(4), NumberNode(5)))

	def test_ternary_in_truthy(self):
		tokens = [
			Token(TokenType.STATEMENT),
			Token(TokenType.LPAREN),
			Token(TokenType.VARIABLE, 'var_3'),
			Token(TokenType.EQUALTO),
			Token(TokenType.NUMBER,4),
			Token(TokenType.TRUTHY),
			Token(TokenType.STATEMENT),
			Token(TokenType.LPAREN),
			Token(TokenType.VARIABLE, 'var_2'),
			Token(TokenType.EQUALTO),
			Token(TokenType.NUMBER,3),
			Token(TokenType.TRUTHY),
			Token(TokenType.NUMBER,4),
			Token(TokenType.FALSY),
			Token(TokenType.NUMBER,5),
			Token(TokenType.RPAREN),
			Token(TokenType.FALSY),
			Token(TokenType.NUMBER,5),
			Token(TokenType.RPAREN),
		]
		node = Parser(tokens).parse()
		self.assertEqual(node,
			ComparisonNode(NumberNode(4), NumberNode(4), ComparisonNode(NumberNode(3), NumberNode(3), NumberNode(4), NumberNode(5)), NumberNode(5))
			)

	def test_ternary_in_falsy(self):
		tokens = [
			Token(TokenType.STATEMENT),
			Token(TokenType.LPAREN),
			Token(TokenType.VARIABLE, 'var_3'),
			Token(TokenType.EQUALTO),
			Token(TokenType.NUMBER,3),
			Token(TokenType.TRUTHY),
			Token(TokenType.NUMBER,5),
			Token(TokenType.FALSY),
			Token(TokenType.STATEMENT),
			Token(TokenType.LPAREN),
			Token(TokenType.VARIABLE, 'var_2'),
			Token(TokenType.EQUALTO),
			Token(TokenType.NUMBER,3),
			Token(TokenType.TRUTHY),
			Token(TokenType.NUMBER,4),
			Token(TokenType.FALSY),
			Token(TokenType.NUMBER,5),
			Token(TokenType.RPAREN),
			Token(TokenType.RPAREN),
		]
		node = Parser(tokens).parse()
		self.assertEqual(node,
			ComparisonNode(NumberNode(4), NumberNode(3), NumberNode(5), ComparisonNode(NumberNode(3), NumberNode(3), NumberNode(4), NumberNode(5)))
			)


	def test_all(self):
		tokens = [
			Token(TokenType.INPUTSTART),
			Token(TokenType.VARIABLE, 'var_1'),
			Token(TokenType.IS_ASSIGNED),
			Token(TokenType.NUMBER, 2),
			Token(TokenType.VARIABLE, 'var_2'),
			Token(TokenType.IS_ASSIGNED),
			Token(TokenType.NUMBER, 3),
			Token(TokenType.VARIABLE, 'var_3'),
			Token(TokenType.IS_ASSIGNED),
			Token(TokenType.NUMBER, 4),
			Token(TokenType.VARIABLE, 'var_4'),
			Token(TokenType.IS_ASSIGNED),
			Token(TokenType.NUMBER, 5),
			Token(TokenType.INPUTEND),
			Token(TokenType.STATEMENT),
			Token(TokenType.LPAREN),
			Token(TokenType.VARIABLE, 'var_1'),
			Token(TokenType.EQUALTO),
			Token(TokenType.NUMBER,3),
			Token(TokenType.TRUTHY),
			Token(TokenType.NUMBER,5),
			Token(TokenType.FALSY),
			Token(TokenType.STATEMENT),
			Token(TokenType.LPAREN),
			Token(TokenType.VARIABLE, 'var_2'),
			Token(TokenType.EQUALTO),
			Token(TokenType.NUMBER,3),
			Token(TokenType.TRUTHY),
			Token(TokenType.NUMBER,4),
			Token(TokenType.FALSY),
			Token(TokenType.NUMBER,5),
			Token(TokenType.RPAREN),
			Token(TokenType.RPAREN),
			Token(TokenType.PLUS),
			Token(TokenType.STATEMENT),
			Token(TokenType.LPAREN),
			Token(TokenType.VARIABLE, 'var_2'),
			Token(TokenType.EQUALTO),
			Token(TokenType.NUMBER,3),
			Token(TokenType.TRUTHY),
			Token(TokenType.NUMBER,4),
			Token(TokenType.FALSY),
			Token(TokenType.NUMBER,5),
			Token(TokenType.RPAREN),
			Token(TokenType.MINUS),
			Token(TokenType.STATEMENT),
			Token(TokenType.LPAREN),
			Token(TokenType.VARIABLE, 'var_3'),
			Token(TokenType.EQUALTO),
			Token(TokenType.NUMBER,3),
			Token(TokenType.TRUTHY),
			Token(TokenType.NUMBER,4),
			Token(TokenType.FALSY),
			Token(TokenType.NUMBER,5),
			Token(TokenType.RPAREN),
			Token(TokenType.PLUS),
			Token(TokenType.STATEMENT),
			Token(TokenType.LPAREN),
			Token(TokenType.VARIABLE, 'var_4'),
			Token(TokenType.EQUALTO),
			Token(TokenType.NUMBER,3),
			Token(TokenType.TRUTHY),
			Token(TokenType.NUMBER,4),
			Token(TokenType.FALSY),
			Token(TokenType.NUMBER,5),
			Token(TokenType.RPAREN),
		]
		node = Parser(tokens).parse()
		self.assertEqual(node, AddNode(
			SubtractNode(
			AddNode(
				ComparisonNode(NumberNode(2), NumberNode(3), NumberNode(5), ComparisonNode(NumberNode(3), NumberNode(3), NumberNode(4), NumberNode(5))),
				ComparisonNode(NumberNode(3), NumberNode(3), NumberNode(4), NumberNode(5))
			), 
				ComparisonNode(NumberNode(4), NumberNode(3), NumberNode(4), NumberNode(5))
			),
			ComparisonNode(NumberNode(5), NumberNode(3), NumberNode(4), NumberNode(5))
			))
