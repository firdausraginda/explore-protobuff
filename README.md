# explore-proto

# references
* tutorial: https://www.youtube.com/watch?v=46O73On0gyI&list=LL&index=1&t=24s
* python protobuff: https://developers.google.com/protocol-buffers/docs/pythontutorial
* protobuff last release: https://github.com/protocolbuffers/protobuf/releases/tag/v3.19.3

# usage
* compile .proto file format: `<path_to_protoc> --python_out=<path_to_destination_file> <path_to_.proto_file>`
* compile .proto file using [protoc](https://github.com/protocolbuffers/protobuf/releases/tag/v3.19.3): `~/Downloads/protoc-3.19.3-osx-x86_64/bin/protoc --python_out=./ ./employees.proto`