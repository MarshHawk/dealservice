# Deal Service
## Description
Using Deuces library for dealing in writing a poker app (TODO: more details on this to come as needed). Create a grpc service to handle deal calls from the bff written in a different language (not python).

```python
>>> import grpc
>>> from proto.hand_pb2 import (HandRequest)
>>> from proto.hand_pb2_grpc import DealerStub
>>> channel = grpc.insecure_channel("localhost:5005")
>>> client = DealerStub(channel)
>>> req=HandRequest(playerCount=5)
>>> hand = client.Deal(req)
>>> print(hand)

board {
  flop: "Th"
  flop: "Jh"
  flop: "6s"
  turn: "4d"
  river: "8h"
}
hands {
  cards: "8s"
  cards: "Ad"
  score: 0.3748324845885822
  description: "Pair"
}
hands {
  cards: "3c"
  cards: "2s"
  score: 0.029348700080407353
  description: "High Card"
}
hands {
  cards: "8c"
  cards: "4c"
  score: 0.5804073974805681
  description: "Two Pair"
}
hands {
  cards: "2c"
  cards: "Kc"
  score: 0.08791208791208793
  description: "High Card"
}
hands {
  cards: "Jd"
  cards: "5d"
  score: 0.4465290806754222
  description: "Pair"
}
```

## Setup
if using conda, create a new environment and install the requirements with conda not pip on arm1 Macs or non-conda Python