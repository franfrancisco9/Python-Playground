# Python-Playground
A repository to test and implement python challenges and tasks.

## Launching the docker container
To launch the docker container, run the following command in the root directory of the repository:

Windows:
```bash
docker build --tag test . ; docker run -it --rm -p 8000:8000 test
```

Linux:
```bash
docker build --tag test . && docker run -it --rm -p 8000:8000 test
```

It will allow a connection on localhost:8000 to the container where you can use task 1A caesar cipher and task 2 island finder. 

