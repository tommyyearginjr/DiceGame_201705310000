import random
from collections import Counter

class Dice (object):
	def __init__(self):
		self.die = list(x for x in range(1,7))
	def roll(self):
		return random.choice(self.die)
		
def TestDie():
	Die01 = Dice()
	Die01_Roll_Results = list(Die01.roll() for x in range(1,101))
	zztop = Counter(Die01_Roll_Results)
	zztop_sorted = sorted(zztop.items())
	for i in zztop_sorted:
		steffi_graf = (i[1] * 'z')
		display = '{}. {}'.format(str(i[0]), steffi_graf)
		print(display)
	Play_Again_Loop()
		
def Play_Again_Loop():
	ask = input('\n\nPlay again? ')
	if ask == 'y':
		print('\n')
		TestDie()
	else:
		print('\nbye')
		
TestDie()
