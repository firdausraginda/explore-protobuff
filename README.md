# explore-proto

# references
* tutorial: https://www.youtube.com/watch?v=46O73On0gyI&list=LL&index=1&t=24s
* python protobuf: https://developers.google.com/protocol-buffers/docs/pythontutorial
* protobuf last release: https://github.com/protocolbuffers/protobuf/releases/tag/v3.19.3

# dependency
* download the proto compiler: https://github.com/protocolbuffers/protobuf/releases/tag/v3.19.3
* install google protobuf: `pipenv install protobuf`
# how to use proto compiler
1. open the proto folder (protoc-3.19.3-osx-x86_64) -> bin -> run the **protoc**
2. compile .proto file: `~/Downloads/protoc-3.19.3-osx-x86_64/bin/protoc --python_out=./ ./employees.proto`