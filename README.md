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

It will allow a connection on `localhost:8000` to the container where you can use task 1A caesar cipher and task 2 island finder. 

After that you should be able to access your browser at `localhost:8000` and see the pages shown below.

## Main page:
`localhost:8000/`

![Main page](./Task%201B/task1b.png)

## Caesar cipher:
`localhost:8000/caesar/encrypt?message=HELLO`

![Caesar cipher](./Task%201A/task1a_enc.png)

`localhost:8000/caesar/decrypt?message=EBIIL`

![Caesar cipher](./Task%201A/task1a_dec.png)

## Island finder:
`localhost:8000/island_finder`

![Island finder](./Task%202/task2.png)