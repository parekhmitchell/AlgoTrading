## Class for handling basic trading actions

# Class declaration
class tradingAccount(object):

	# creates object with balance, numContracts
	# TODO: implement account performance
	def __init__(self, initalBalance):
		self.balance = initalBalance;
		self.numContracts = 0;

	# buy amt$ of contract at currentPrice
	def buyAmount(self, amt, currentPrice):
		if(currentPrice > amt or amt > self.balance):
			print("Could not place trade");
			return;

		self.numContracts += (amt/currentPrice);
		self.balance -= self.numContracts * currentPrice;

	# buy maximum amount of contracts at currentPrice
	def buyAll(self, currentPrice):
		if(currentPrice > self.balance):
			print("Could not place trade");
			return;

		self.numContracts += (self.balance/currentPrice);
		self.balance -= self.numContracts * currentPrice;

	# clear out positions and liquidate account
	def liquidate(self, currentPrice):
		if(self.numContracts <= 0):
			print("Could not liquidate account");
			return;

		self.balance += self.numContracts * currentPrice;
		self.numContracts = 0;

	# return current balance
	def getBalance(self):
		return self.balance;

	# return current number of contracts
	def getContracts(self):
		return self.numContracts;
