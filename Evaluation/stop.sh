#Containers stop
docker stop planner worker
docker rm planner worker
#Network stop
docker network rm dockerNetwork