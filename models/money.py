# This class defines a Money card
# The bills come in $1, $2, $3, $4, $5 and $10 denominations
from card import Card

class MoneyCard(Card):
	def __init__(self, denomination):
		# Initialize a money card
		super().__init__("money")	
		self.denomination = denomination
