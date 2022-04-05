import grpc
import calc_pb2_grpc
import calc_pb2
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


result = 0

with grpc.insecure_channel(f'{HOST}:{PORT}') as channel:
	stub = calc_pb2_grpc.CalculatorStub(channel)
	
	if operation == '+':
		result = stub.Add(calc_pb2.CalculatorRequest(op1=first_operand, op2=second_operand))
	elif operation == '-':
		result = stub.Add(calc_pb2.CalculatorRequest(op1=first_operand, op2=second_operand))
	elif operation == '*':
		result = stub.Add(calc_pb2.CalculatorRequest(op1=first_operand, op2=second_operand))
	elif operation == '/':
		result = stub.Add(calc_pb2.CalculatorRequest(op1=first_operand, op2=second_operand))
	else:
		print('Invalid operation')
		exit()

print(result)
