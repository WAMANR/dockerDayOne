docker network create dockerNetwork

docker run --network=dockerNetwork -e HOST=registry -e PORT=8080 --name registry -d registry
docker run --network=dockerNetwork -e HOST=broker -e PORT=1111 -e REGISTRY=http://registry:8080 -e ADRESS=http://broker --name broker -d broker
docker run --network=dockerNetwork -e HOST=s1 -e PORT=4567 -e REGISTRY=http://registry:8080 -e ADRESS=http://s1 --name s1 -d s1
docker run --network=dockerNetwork -e HOST=s2 -e PORT=5372 -e REGISTRY=http://registry:8080 -e ADRESS=http://s2 --name s2 -d s2