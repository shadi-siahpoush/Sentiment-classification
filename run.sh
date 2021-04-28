sudo y| docker system prune -a
sudo docker build -t test .
sudo docker run -it test
