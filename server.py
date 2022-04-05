from concurrent import futures
import grpc
import calc_pb2_grpc
import calc_pb2
from constCS import * #-

class Calculator(calc_pb2_grpc.CalculatorServicer):
	def Mult(self, request, context):
		op1 = request.op1
		op2 = request.op2
		result = op1 * op2
		return calc_pb2.CalculatorReply(response=result)

	def Div(self, request, context):
		op1 = request.op1
		op2 = request.op2
		result = op1 / op2
		return calc_pb2.CalculatorReply(response=result)
	
	def Sub(self, request, context):
		op1 = request.op1
		op2 = request.op2
		result = op1 - op2
		return calc_pb2.CalculatorReply(response=result)
	
	def Add(self, request, context):
		op1 = request.op1
		op2 = request.op2
		result = op1 + op2
		return calc_pb2.CalculatorReply(response=result)
	

if __name__ == "__main__":
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	calc_pb2_grpc.add_CalculatorServicer_to_server(
		Calculator(), server
	)
	server.add_insecure_port(f'[::]:{PORT}')
	server.start()
	server.wait_for_termination()
