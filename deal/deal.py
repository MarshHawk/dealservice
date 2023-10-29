from concurrent import futures
import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import InvalidArgument
from proto import hand_pb2_grpc
from builder import build_deal_payload

class DealService(hand_pb2_grpc.DealerServicer):
    def Deal(self, request, context):
        print('deal')
        if request.playerCount > 6:
            raise InvalidArgument("Hands with more than 6 players not supported")

        return build_deal_payload(request.playerCount)

def serve():
    print('serve')
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    hand_pb2_grpc.add_DealerServicer_to_server(
        DealService(), server
    )
    server.add_insecure_port("[::]:50053")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
