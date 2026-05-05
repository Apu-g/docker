#this is the docker tutorial

#to make a docker image - we have to run a command in the terminal

docker build -t <name of the image here>:<version if we want> .
docker build -t first_app .    

#the . dot is for loading all the files into the image and the -t is for creating the name of the image

# also to run the docker file we run the following cmd

docker run --name <name of the container to make> <name of the image>
 docker run --name first_container first_app
#running this will give us the output if we want to run the interactive session we can run the below cmd

docker run -it --name <name of the container to make> <name of the image> /bin/sh
docker run -it --name first_container1 first_app /bin/sh

