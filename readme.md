# this is the docker tutorial

# to make a docker image - we have to run a command in the terminal

docker build -t <name of the image here>:<version if we want> .
docker build -t first_app .    

# the . dot is for loading all the files into the image and the -t is for creating the name of the image

# also to run the docker file we run the following cmd

docker run --name <name of the container to make> <name of the image>
docker run --name first_container first_app
# running this will give us the output if we want to run the interactive session we can run the below cmd

docker run -it --name <name of the container to make> <name of the image> /bin/sh
docker run -it --name first_container1 first_app /bin/sh


# to see the docker container running
docker ps

# to see the docker container that exist 
docker ps -a

# to stop the docker container
docker stop <container id>

# to remove the docker container
docker rm <container id>

# to view the images in the docker 
docker image ls

# to remove an image in the docker
docker rmi <image name>

# when we make a flask application we need to do the post mapping - so make sure we need to map the right port to the local machine with the docker container port 
docker run -p <port no>:<port no> --name <container name> <image name>
docker run -p 5000:5000 --name flask flask_image
# this will help us to run the app in the docker with using the same port as the local machine and the docker port

# To make a sql docker file you have to do this 

#pull official mysql image
FROM mysql:latest

#set environment variables
ENV MYSQL_ROOT_PASSWORD=rootpassword
ENV MYSQL_DATABASE=mydatabase

#copy the initialization script to the container
COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 3307

# and then in innit.sql you have to write the sql code for the execution when the container is run

# To run a mysql file in the docker container and execute it in the terminal run this command
docker exec -it  mysql_container mysql -u root -p

# see the available networks in docker 
docker network ls

# to create a network in docker 
docker network create network_name

# creation of a yml file for the docker compose  - it basically makes sure that we can make a network automatically and all the services are included in the docker compose file that checks the interval and makes sure each is running before the other can function


# some commands
# this helps to start the container nothing on creating it
docker compose up -d

# to make or build an image
docker compose up -d 

# to remove a container 
docker compose down

# to rebuild a container 
docker compose up -d --build


# docker volumes - are like storing the data in docker and used in the containers and make sure the container is called with the container so that we can acces the data and if the volume is nor used then the data is not in the container and once due to this docker volumes are not in the image its in the container
