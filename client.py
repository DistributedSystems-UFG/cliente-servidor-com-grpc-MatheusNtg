import pickle
import os
from socket  import *
from constCS import * #-

possible_ops = {
	1: 'For add         type "+"',
	2: 'For multiply    type "*"',
	3: 'For subtraction type "-"',
	4: 'For division    type "/"',
}

def print_op_usage():
	for op in possible_ops.values():
		print(op)

print_op_usage()
operation = str(input("Chose you operation: "))
first_operand = int(input("Type the first operand (integers only): "))
second_operand = int(input("Type the second operand (integers only): "))

conn = rpyc.connect(SERVER, PORT) # Connect to the server
result = 0

if operation == '+':
    result = conn.root.exposed_sum(first_operand, second_operand)
elif operation == '-':
	result = conn.root.exposed_sub(first_operand, second_operand)
elif operation == '*':
    result = conn.root.exposed_mult(first_operand, second_operand)
elif operation == '/'
	result = conn.root.exposed_div(first_operand, second_operand)
else:
	print('Invalid operation')
	os.exit()

print(f'Answer: {result}')
