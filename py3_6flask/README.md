# Python 3.6.4,Flask, Alpine Linux and Redis within Containers

Here a Dockerfile that use a image including Python and Flask within Alpine and Redis to store data in cache. 

## Installing Docker

Ubuntu/Debian

```
sudo apt-get -y update && apt-get install -y docker.io
```

CentOS

```
yum install -y docker.io
```


## Installing Docker Compose

```
sudo curl -L https://github.com/docker/compose/releases/download/1.18.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
```

then

```
sudo chmod +x /usr/local/bin/docker-compose
```

Test the installation

```
$ docker-compose --version
docker-compose version 1.18.0, build 1719ceb
```



**Note:** If you have Docker 1.12.6 menor or equal  please modify the version of docker-compose to 2 otherwise type version 3 within docker-compose.yml 


Before Deploy:

**CentOS:**  ``` setenforce 0 ```

**Ubuntu:** ```sudo ufw allow 5000 ```
           

           ``` ufw reload ```

## Deploying

```
docker-compose up
```

Now you can see in your browser typing localhost:5000 


