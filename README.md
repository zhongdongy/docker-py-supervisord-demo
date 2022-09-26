## Usage of the example

Please download/clone the source code, then make some changes to the Python script `main.py`. 

### Steps of build
```bash
docker build --no-cache -t test/test:latest .
```

### Start a container with new image
```bash
docker run --name "test" --env LOG_LEVEL=DEBUG -d --rm test/test:latest
```

Node: you might want to change `test/test:latest` to something else.

To examine the status of your program (`main.py`), enter the running container, then check status by:
```bash
docker exec -it test /bin/bash
supervisorctl status demo_app
```