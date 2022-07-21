from concurrent import futures
import time
import grpc
from grpc import ServicerContext
import gamma_pb2_grpc
import gamma_pb2
from gamma_pb2 import Status, StatusCheckRequest, QueryPassagePair, FoundAnswers, \
    QueryWithPassages, FoundAnswersForPassages
import json
from primeqa.primeqa.pipelines.extractive_mrc_pipeline import MRCPipeline
reader = MRCPipeline("PrimeQA/tydiqa-primary-task-xlm-roberta-large")
# import greet_pb2
# import greet_pb2_grpc

class ReadingComprehensionServicer(gamma_pb2_grpc.ReadingComprehensionServicer):
    def FindAnswers(self, request, context):
        question = "Which country is Canberra located in?"
        context = """Canberra is the capital city of Australia. 
        Founded following the federation of the colonies of Australia 
        as the seat of government for the new nation, it is Australia's 
        largest inland city"""
        answers = reader.predict(question, context)
        return print(json.dumps(answers, indent=4))
    # class GreeterServicer(greet_pb2_grpc.GreeterServicer):
#     def SayHello(self, request, context):
#         print("SayHello Request Made: \n")
#         print(request)
#         hello_reply=greet_pb2.HelloResponse()
#         hello_reply.message = f"{request.greeting} there {request.name}!"
#         return hello_reply
#
#     def ParrotSaysHello(self, request, context):
#         print("ParrotSaysHello Request Made: \n")
#         print(request)
#         for i in range(3):
#             hello_reply = greet_pb2.HelloResponse()
#             hello_reply.message = '%s there %s! %s' %(request.greeting, request.name, (i+1))
#             yield hello_reply
#             time.sleep(3)
#
#     def ChattyClientSaysHello(self, request_iterator, context):
#         delayed_response = greet_pb2.DelayedResponse()
#         for request in request_iterator:
#             print("ChattyClientSaysHello Request Made: \n")
#             print(request)
#             delayed_response.request.append(request)
#         delayed_response.message = f"You have sent {len(delayed_response.request)} requests. Please expect a delayed reply."
#         return delayed_response
#
#
#
#     def InteractingHello(self, request_iterator, context):
#         for request in request_iterator:
#             print("InteractingHello Request Made: \n")
#             print(request)
#
#             hello_reply = greet_pb2.HelloResponse()
#             hello_reply.message = f"{request.greeting} there {request.name}!"
#             yield hello_reply


def serve():
    host = "localhost:50052"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    gamma_pb2_grpc.add_ReadingComprehensionServicer_to_server(ReadingComprehensionServicer(), server)
    #greet_pb2_grpc.add_GreeterServicer_to_server(GreeterServicer(), server)
    server.add_insecure_port(host)
    server.start()
    print("Listening at %s" %(host) )
    server.wait_for_termination()   

if __name__ == '__main__':
    serve()