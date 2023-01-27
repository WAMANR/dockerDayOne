#Network run
docker network create dockerNetwork
#Containers runs
#Command arguments : WORKER STARTING PORT, TASKS, GENERALS WORKERS, ADDITION WORKERS, MULTIPLICATION WORKERS
sh workersRun.sh 1000 5 2 0 0

