#Network run
docker network create dockerNetwork
#Containers runs
docker run --network=dockerNetwork --name worker -d worker
docker run --network=dockerNetwork -e PORT=3000 -e TASKS=4 --name planner -d planner