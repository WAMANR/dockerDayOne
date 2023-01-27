#Containers stop
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
#Network stop
docker network rm dockerNetwork