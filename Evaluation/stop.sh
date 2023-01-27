#Containers stop
docker stop planner worker0 worker1
docker rm planner worker0 worker1
#Network stop
docker network rm dockerNetwork