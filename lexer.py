from tokens import Token, TokenType

WHITESPACE = ' \n\t'
DIGITS = '0123456789'
OPERATOR ='iIfF'
CONTAINER = '\{\}'
SIGN= '=<>'
VARIABLE = 'varVAR_12345'
comma_count = 0
compy =None

class Lexer:

	def __init__(self, text):
		self.text = iter(text)
		self.advance()

	def advance(self):
		try:
			self.current_char=  next(self.text)
		except StopIteration:
			self.current_char = None

	def generate_tokens(self):
		while self.current_char != None:
			if self.current_char in WHITESPACE:
				self.advance()
			elif self.current_char == '.' or self.current_char in DIGITS:
				yield self.generate_number()
			elif self.current_char in OPERATOR: 
				yield self.confirm_ternary()
			elif self.current_char in VARIABLE: 
				yield self.var_name()
			elif self.current_char == '+':
				self.advance()
				yield Token(TokenType.PLUS)
			elif self.current_char == '-':
				self.advance()
				yield Token(TokenType.MINUS)
			elif self.current_char == '*':
				self.advance()
				yield Token(TokenType.MULTIPLY)
			elif self.current_char == '/':
				self.advance()
				yield Token(TokenType.DIVIDE)
			elif self.current_char == '(':
				self.advance()
				yield Token(TokenType.LPAREN)
			elif self.current_char == ')':
				self.advance()
				yield Token(TokenType.RPAREN)
			elif self.current_char == '{':
				self.advance()
				yield Token(TokenType.INPUTSTART)
			elif self.current_char == '}':
				self.advance()
				yield Token(TokenType.INPUTEND)
			elif self.current_char == '=':
				yield self.check_equal_or_assign()
			elif self.current_char == ',':
				checker = self.check_if_else()
				if checker != None:
					yield checker
				else:
					self.advance()
			elif self.current_char == ':':
				self.advance()
				yield Token(TokenType.IS_ASSIGNED)
			else:
				raise Exception(f"Illegal character '{self.current_char}'")

	def generate_number(self):
		decimal_point_count = 0
		number_str = self.current_char
		self.advance()
		while self.current_char != None and (self.current_char == '.' or self.current_char in DIGITS):
			if self.current_char == '.':
				decimal_point_count += 1
				if decimal_point_count > 1:
					break
			
			number_str += self.current_char
			self.advance()

		if number_str.startswith('.'):
			number_str = '0' + number_str
		if number_str.endswith('.'):
			number_str += '0'

		return Token(TokenType.NUMBER, int(number_str))

	def var_name(self):
		var_str = self.current_char
		self.advance()
		
		while self.current_char is not None and (self.current_char in VARIABLE or self.current_char in DIGITS):
			  var_str += self.current_char
			  self.advance()

		return Token(TokenType.VARIABLE, var_str)

	def confirm_ternary(self):
		str_count = 0

		while self.current_char != None and self.current_char in OPERATOR:
			if self.current_char == 'I' or self.current_char == 'i':
				str_count += 1
				self.advance()

			if str_count == 1 and (self.current_char == 'F' or self.current_char == 'f'):
				str_count += 1
				self.advance()

			if str_count > 1:
				break
		return Token(TokenType.STATEMENT)

	def check_if_else(self):
		global comma_count
		global compy
		
		if self.current_char is not None and self.current_char == ',' and compy=='equate':
			if  comma_count == 0:
				self.advance()
				comma_count += 1
				return Token(TokenType.TRUTHY)

			if comma_count == 1:
				self.advance()
				comma_count = 0
				compy = None

				return Token(TokenType.FALSY)

		# else: 
		# 	return

	def check_equal_or_assign(self):
		eq_count = 0
		global compy

		while self.current_char != None and self.current_char in SIGN:
			if self.current_char == '=':
				eq_count += 1
				self.advance()

			if eq_count == 1 and self.current_char == '=':
				self.advance()
				compy = 'equate'
				eq_count += 1
				return Token(TokenType.EQUALTO)
			
			if eq_count > 1:
				break
                

