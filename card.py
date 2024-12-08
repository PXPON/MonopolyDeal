# This class will define the Cards used in Monopoly Deal

class Card:
	# Cards can be of the following types:
	# Cash cards (1, 5, or 10)
	# Property Cards (Boardwalk, etc.)
	# Action Cards (Pass Go, Collect Rent, etc.)
	def __init__(self, type):
		self.type = type

