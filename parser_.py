from tokens import TokenType
from node import * 

var_samp= []
input_=[]

class Parser:
	def __init__(self, tokens):
		self.tokens = iter(tokens)
		self.advance()

	def raise_error(self):
		raise Exception("Invalid syntax")
	
	def advance(self):
		try:
			self.current_token = next(self.tokens)
		except StopIteration:
			self.current_token = None

	def parse(self):
		if self.current_token == None:
			return None

		result = self.expr()
		if self.current_token != None:
			self.raise_error()

		return result

	def expr(self):
		result = self.term()

		while self.current_token != None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
			if self.current_token.type == TokenType.PLUS:
				self.advance()
				result = AddNode(result, self.term())
			elif self.current_token.type == TokenType.MINUS:
				self.advance()
				result = SubtractNode(result, self.term())

		return result

	def term(self):
		token = self.current_token
		if token.type == TokenType.INPUTSTART:
			self.cmpare_()	 

		token = self.current_token
		if token.type == TokenType.STATEMENT:
			result=self.ternary()
			self.advance()
			
		return result

	def cmpare_(self):

		token = self.current_token
		if token.type == TokenType.INPUTSTART:
			token = self.current_token
			while token.type != TokenType.INPUTEND:
				self.advance()
				token = self.current_token
				if token != None:
					if token.type == TokenType.VARIABLE:
						res = token.value
						var_samp.append(res)
					elif token.type == TokenType.IS_ASSIGNED:
						self.advance()
						token = self.current_token
						if token.type == TokenType.NUMBER:
							rslt= NumberNode(token.value)
							input_.append(rslt)
			self.advance()

	def ternary(self):
		self.advance()
		token = self.current_token
		if token.type == TokenType.LPAREN:
			token = self.current_token
			while token.type != TokenType.RPAREN:
				self.advance()
				token = self.current_token
				if token != None:
					if token.type == TokenType.VARIABLE:
						res = token.value
						try:
							rsltt= var_samp.index(res)
							rzult = input_[rsltt]
							locals() [res] = rzult
						except:
							raise Exception(f" one input not declared or input doesn't match")
					elif token.type == TokenType.EQUALTO:
						self.advance()
						token = self.current_token
						if token.type == TokenType.NUMBER: 
							rslt= NumberNode(token.value)
					elif token.type == TokenType.TRUTHY:
						self.advance()
						token = self.current_token
						truthy= NumberNode(token.value)
					elif token.type == TokenType.FALSY:
						self.advance()
						token = self.current_token
						if token.type == TokenType.NUMBER:
							falsy = NumberNode(token.value)
						elif token.type == TokenType.STATEMENT:
							falsy = self.ternary()
			result = ComparisonNode(rzult,rslt,truthy,falsy)
		return result
