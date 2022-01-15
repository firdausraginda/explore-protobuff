# explore-proto

# references
* tutorial: https://www.youtube.com/watch?v=46O73On0gyI&list=LL&index=1&t=24s
* python protobuff: https://developers.google.com/protocol-buffers/docs/pythontutorial
* protobuff last release: https://github.com/protocolbuffers/protobuf/releases/tag/v3.19.3

# how to use proto compiler
1. download the proto compiler: https://github.com/protocolbuffers/protobuf/releases/tag/v3.19.3
2. open the proto folder -> bin -> run the **protoc**
3. compile .proto file: `~/Downloads/protoc-3.19.3-osx-x86_64/bin/protoc --python_out=./ ./employees.proto`