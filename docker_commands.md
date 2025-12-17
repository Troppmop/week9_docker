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

```docker run -it --name shopping-server-app1 -v fastapi-db:/app/db shopping-server1:v1

## Server 2

### Build the image

```bash

```C:\Users\Dovid\Desktop\data_army\week9\week9_docker\server2>docker build -t shopping-server2:v1 .

### Run the container

```bash

```docker run -it --name shopping-server-app2 -v fastapi-db:/app/db shopping-server2:v1

