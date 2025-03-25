docker build --no-cache -t jdr-server .
docker run -p 5000:5000 --name jdr-container jdr-server

# sudo kill -9 $(docker inspect --format='{{.State.Pid}}' 69ce904eb21b)