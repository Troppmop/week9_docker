# Docker Commands

Fill in the Docker commands you used to complete the test.

## Volume

### Create the volume

```bash

```docker volume create fastapi-db

### Seed the volume (via Docker Desktop)

```bash

```

## Server 1

### Build the image

```bash

```C:\Users\Dovid\Desktop\data_army\week9\week9_docker\server1>docker build -t shopping-server1:v1 .

### Run the container

```bash

```docker run -it --name shopping-server1 -v fastapi-db:/app/db alpine sh

## Server 2

### Build the image

```bash

```

### Run the container

```bash

```

