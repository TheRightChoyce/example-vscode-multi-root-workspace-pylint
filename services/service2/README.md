## To build the docker image:
    docker build --tag vscode-multi-root-service2 .  

## To run docker:
    docker run -d \
        -p 5002:5002 \
        --name service2 \
        vscode-multi-root-service2