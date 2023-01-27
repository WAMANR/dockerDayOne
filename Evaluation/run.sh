#Network run
docker network create dockerNetwork
#Containers runs
docker run --network=dockerNetwork -e ADD=true -e MULT=false -e PORT=8080 --name workerAdd -d worker
docker run --network=dockerNetwork -e ADD=false -e MULT=true -e PORT=8081 --name workerMult -d worker
docker run --network=dockerNetwork -e PORT=3000 -e TASKS=20 --name planner -d planner