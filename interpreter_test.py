import unittest
from node import *
from interpreter import Interpreter
from values import Number

class TestInterpreter(unittest.TestCase):

	def test_numbers(self):
		value = Interpreter().visit(NumberNode(10))
		self.assertEqual(value, Number(10))

	def test_single_operations(self):
		result = Interpreter().visit(AddNode(NumberNode(2), NumberNode(4)))
		self.assertEqual(result.value, 6)

		result = Interpreter().visit(SubtractNode(NumberNode(7), NumberNode(4)))
		self.assertEqual(result.value, 3)

		result = Interpreter().visit(MultiplyNode(NumberNode(2), NumberNode(4)))
		self.assertEqual(result.value, 8)

		result = Interpreter().visit(DivideNode(NumberNode(8), NumberNode(4)))
		self.assertAlmostEqual(result.value, 2)

		with self.assertRaises(Exception):
			Interpreter().visit(DivideNode(NumberNode(2), NumberNode(0)))

	def test_expression(self):
		tree = ComparisonNode(NumberNode(4), NumberNode(3), NumberNode(4), NumberNode(5))
		result = Interpreter().visit(tree)
		self.assertEqual(result.value, 5)

	def test_ternary_truthy(self):
		tree = ComparisonNode(NumberNode(4), NumberNode(4), ComparisonNode(NumberNode(3), NumberNode(3), NumberNode(4), NumberNode(5)), NumberNode(5))
		result = Interpreter().visit(tree)
		self.assertEqual(result.value, 4)

	def test_ternary_falsy(self):
		tree = ComparisonNode(NumberNode(4), NumberNode(3), NumberNode(5), ComparisonNode(NumberNode(3), NumberNode(3), NumberNode(4), NumberNode(5)))
		result = Interpreter().visit(tree)
		self.assertEqual(result.value, 4)

	def test_full_expression(self):
		tree = AddNode(
			SubtractNode(
			AddNode(
				ComparisonNode(NumberNode(2), NumberNode(3), NumberNode(5), ComparisonNode(NumberNode(3), NumberNode(3), NumberNode(4), NumberNode(5))),
				ComparisonNode(NumberNode(3), NumberNode(3), NumberNode(4), NumberNode(5))
			), 
				ComparisonNode(NumberNode(4), NumberNode(3), NumberNode(4), NumberNode(5))
			),
			ComparisonNode(NumberNode(5), NumberNode(3), NumberNode(4), NumberNode(5))
			)

		result = Interpreter().visit(tree)
		self.assertEqual(result.value, 8)
