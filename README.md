import grpc
from hand_pb2 import (HandRequest)
from hand_pb2_grpc import DealerStub
channel = grpc.insecure_channel("localhost:50053")
client = DealerStub(channel)
req=HandRequest(playerCount=3)
client.Deal(req)

python -m grpc_tools.protoc -I ../protobufs --python_out=. \
         --grpc_python_out=. ../protobufs/hand.protoprint(client)

from builder import build_deal_payload
build_deal_payload(3)