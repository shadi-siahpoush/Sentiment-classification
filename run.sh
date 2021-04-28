sudo y| docker system prune -a # removed all the images
sudo docker build -t test . # build image from the dockerfile in the curent folder
sudo docker image list # show if the image has been created
sudo docker run -it test # run the image after it is created
