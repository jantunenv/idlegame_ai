import numpy as np

class Idlegame:
	money = 0.0
	income = 0.0
	upgrade_base_prices = np.asarray([1.0, 10.0, 100.0, 1000.0, 10000.0])
	upgrade_levels = np.asarray([0.0, 0.0, 0.0, 0.0, 0.0])
	updgrade_price_multipliers = np.asarray([1.1, 1.1, 1.1, 1.1, 1.1])
	upgrade_prices = np.asarray([1.0, 1.0, 1.0, 1.0, 1.0])
	upgrade_base_income = np.asarray([1.0, 20.0, 300.0, 4000.0, 50000.0])
	
	def __init__(self):
		self.upgrade_prices = self.upgrade_prices*self.upgrade_base_prices
		
	def earn_one_money(self):
		self.money += 1.0
		
	def buy_upgrade(self, n):
		if(n < len(self.upgrade_levels) and n >= 0):
			price = self.upgrade_prices[n]
			if(self.money >= price):
				self.money -= price
				self.upgrade_levels[n] += 1.0
				self.income += self.upgrade_base_income[n]
				self.upgrade_prices[n] = self.upgrade_prices[n]*self.updgrade_price_multipliers[n]
		
	def advance_game(self, player_input=-1):
		match player_input:
			case 0:
				self.earn_one_money()
			case 1:
				self.buy_upgrade(0)
			case 2:
				self.buy_upgrade(1)
			case 3:
				self.buy_upgrade(2)
			case 4:
				self.buy_upgrade(3)
			case 5:
				self.buy_upgrade(4)
			case _:
				pass
		
		self.money += self.income
		
	def get_game_state(self):
		return(self.money, self.income, self.upgrade_prices, self.upgrade_levels, self.upgrade_base_income)
		
def gameloop(game):

	for step in range(20):
		player_input = int(input("Enter player input (0-5)"))
		game.advance_game(player_input)
		state = game.get_game_state()
		print(state[0], state[1], state[2])

def main():
	game = Idlegame()
	gameloop(game)

if __name__ == "__main__":
	main()
