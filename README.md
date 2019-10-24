# UDP Client + Server

### Usage
`$ docker build -t udpserver .`  
`$ docker run -it -p 8080:8080/udp --rm udpserver`  
`$ docker ps  # to list running containers`  
`$ docker kill <container-id>  # to kill server`  
`$ ./client.py  # to run the UDP client`  
