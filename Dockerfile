FROM gcc:latest
COPY . /usr/src/myapp
WORKDIR /usr/src/myapp
RUN gcc -o udpserver udpserver.c
EXPOSE 8080
CMD ["./udpserver", "8080"]