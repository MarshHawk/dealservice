from grpc.tools import protoc

protoc.main(
    (
        '',
        '-I.',
        '--python_out=./client',
        '--grpc_python_out=./client',
        './proto/hand.proto',
    )
)
