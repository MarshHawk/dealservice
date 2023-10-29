from grpc.tools import protoc

protoc.main(
    (
        '',
        '-I.',
        '--python_out=./deal',
        '--grpc_python_out=./deal',
        './proto/hand.proto',
    )
)