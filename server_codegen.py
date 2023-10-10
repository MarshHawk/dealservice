from grpc.tools import protoc

protoc.main(
    (
        '',
        '-I.',
        '--python_out=./server',
        '--grpc_python_out=./server',
        './proto/hand.proto',
    )
)