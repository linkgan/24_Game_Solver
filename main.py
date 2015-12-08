from __future__ import division

import itertools

ANSWER = 24

var = [2,3,5,12]
oper = '*/+-'


class Combo:
	#Initialize combo class storing current number list and operator permutations
	def __init__(self, num_list, oper):
		self.num_list = num_list
		self.oper = oper
		self.result_r = 0
		self.result_c = 0
		self.result_l = 0
		self.valid_r = 0
		self.valid_c = 0
		self.valid_l = 0
		self.num_len = len(self.num_list)
	
	def solve_combo(self):
	#SOLVE for right nested combinations
		for x in range(self.num_len):
			if x == 1:
				self.result_r = operation(self.num_list[x-1],self.num_list[x],self.oper[x-1])
			elif x > 1:
				self.result_r = operation(self.result_r, self.num_list[x], self.oper[x-1])
		if self.result_r == ANSWER:
			self.valid_r = 1
	#SOLVE for left nested combinations	
		for x in range(self.num_len):
			if x == 1:
				self.result_l = operation(self.num_list[x-1],self.num_list[x],self.oper[x-1])
			elif x > 1:
				self.result_l = operation(self.num_list[x],self.result_l, self.oper[x-1])
		if self.result_l == ANSWER:
			self.valid_l = 1
	#SOLVE for center nested combinations		
		temp_1 = operation(self.num_list[0],self.num_list[1], self.oper[0])
		temp_2 = operation(self.num_list[2],self.num_list[3], self.oper[2])
		self.result_c = operation(temp_1,temp_2,self.oper[1])
		
		if self.result_c == ANSWER:
			self.valid_c = 1
			
		return 1
	
	def is_valid_r(self):
		return self.valid_r
	def is_valid_l(self):
		return self.valid_l
	def is_valid_c(self):
		return self.valid_c
	def get_result(self):
		return self.result

#Standard binary operation
def operation(a,b,oper):
	result = 0
	if oper =='*':
		result = a*b
	elif oper == '/':
		if b == 0:
			return result
		result = a/float(b)
	elif oper == '+':
		result = a+b
	elif oper == '-':
		result = float(a-b)
	return result

def main():
	print("solving for ")
	print(var)
	list_combo = []
	
	#Create a list of Combos
	list_perm = list(itertools.permutations(var))
	oper_perm = list(itertools.product(oper,repeat = len(var)-1)) #only 3 binary opers for 4 numbers
	
	n = len(list_perm)
	m = len(oper_perm)
	
	''
	for x in range(n):
		for y in range(m):
			list_combo.append(Combo(list_perm[x], oper_perm[y]))
			list_combo[y+x*m].solve_combo()
	'''
	temp_combo = Combo([3,7,3,7],['/','+','x'])
	temp_combo.solve_combo()
	
	print(temp_combo.num_list, temp_combo.oper)
	print temp_combo.result
	
	'''
	for x in range(n):
		for y in range(m):
			this_combo = list_combo[y+x*m]
			# print this_combo.result
			# print(this_combo.num_list, this_combo.oper)
			if this_combo.is_valid_r() == 1:
				print ('===========SOLVED============ RIGHT')
				print(this_combo.num_list, this_combo.oper)
			if this_combo.is_valid_l() == 1:
				print ('===========SOLVED============ LEFT')
				print(this_combo.num_list, this_combo.oper)
			if this_combo.is_valid_c() == 1:
				print ('===========SOLVED============ CENTER')
				print(this_combo.num_list, this_combo.oper)
			# raw_input()
	''
		
if __name__ == "__main__":
	main()