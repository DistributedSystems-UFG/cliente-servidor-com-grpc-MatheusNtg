from concurrent import futures
import grpc
import calc_pb2_grpc
import calc_pb2
from constCS import * #-

class Calculator(calc_pb2_grpc.CalculatorServicer):
	def Mult(self, request, context):
		print(request.op1)
		return calc_pb2.CalculatorReply(response=0)

	def Div(self, request, context):
		print(request.op1)
		return calc_pb2.CalculatorReply(response=0)
	
	def Sub(self, request, context):
		print(request.op1)
		return calc_pb2.CalculatorReply(response=0)
	
	def Add(self, request, context):
		print(request.op1)
		return calc_pb2.CalculatorReply(response=0)
	

if __name__ == "__main__":
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	calc_pb2_grpc.add_CalculatorServicer_to_server(
		Calculator(), server
	)
	server.add_insecure_port('[::]:50051')
	server.start()
	server.wait_for_termination()
