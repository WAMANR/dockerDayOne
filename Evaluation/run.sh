#Network run
docker network create dockerNetwork
#Containers runs
docker run --network=dockerNetwork -e PORT=8080 --name worker0 -d worker
docker run --network=dockerNetwork -e PORT=8081 --name worker1 -d worker
docker run --network=dockerNetwork -e PORT=3000 -e TASKS=4 --name planner -d planner