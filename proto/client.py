import time
import grpc

import greet_pb2 
import greet_pb2_grpc

def get_client_stream_requests():
    while True:
        name = input('What is your name (or `nothing` to stop chatting)? ')

        if name == '':
            break

        hello_request = greet_pb2.HelloRequest(greeting="Hello", name=name)
        yield hello_request
        time.sleep(1)

def run():
    host = "localhost:50052"
    with grpc.insecure_channel(host) as channel:
        stub = greet_pb2_grpc.GreeterStub(channel)
        print("1. SayHello - Unary")
        print("2. ParrotSaysHello - Server Side Streaming")
        print("3. ChattyClientSaysHello - Client Side Streaming")
        print("4. InteractingHello - Both Streaming")

        rpc_call = input("Which rpc would you like to call? ")

        if rpc_call == "1":
            hello_request = greet_pb2.HelloRequest(greeting = 'Hello', name = input('What is your name? '))
            hello_reply = stub.SayHello(hello_request)
            print("SayHello Response Recieved: \n")
            print(hello_reply)

        elif rpc_call == "2":
            hello_request = greet_pb2.HelloRequest(greeting = 'Hello', name = input('What is your name? '))
            hello_replies = stub.ParrotSaysHello(hello_request)
            print("ParrotSaysHello Response Recieved: \n")
            for hello_reply2 in hello_replies:
                print(hello_reply2)

        elif rpc_call == "3":
            delayed_reply = stub.ChattyClientSaysHello(get_client_stream_requests())
            print("ChattyClientSaysHello Response Recieved: \n")
            print(delayed_reply)
            # for req in delayed_reply.request:
            #     print(req.name)
   
        elif rpc_call == "4":
            responses = stub.InteractingHello(get_client_stream_requests())
            for response in responses:
                print("InteractingHello Response Recieved: \n")
                print(response.message)
        else:
            print("Invalid selection. Choose a number between 1-4.")


if __name__=='__main__':
    run()

