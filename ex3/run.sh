docker network create dockerNetwork

docker run --network=dockerNetwork -e HOST=s3 -e PORT=8080 --name s3 -d s3
docker run --network=dockerNetwork -e HOST=s1 -e PORT=4567 -e S3=http://s3:8080 -e ADRESS=http://s1 --name s1 -d s1
docker run --network=dockerNetwork -e HOST=s2 -e PORT=5372 -e S3=http://s3:8080 -e ADRESS=http://s2 --name s2 -d s2

