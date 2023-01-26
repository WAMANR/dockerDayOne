docker build -f DockerfileS1 -t s1 .
docker build -f DockerfileS2 -t s2 .
docker build -f DockerfileBroker -t broker .
docker build -f DockerfileRegistry -t registry .