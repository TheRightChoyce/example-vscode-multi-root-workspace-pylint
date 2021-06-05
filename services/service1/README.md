## To build the docker image:
    docker build --tag vscode-multi-root-service1 .  

## To run docker:
    docker run \
        -dp 5001:5001 \
        --name service1 \
        vscode-multi-root-service1 