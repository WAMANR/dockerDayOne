#Containers stop
docker stop planner workerAdd workerMult
docker rm planner workerAdd workerMult
#Network stop
docker network rm dockerNetwork