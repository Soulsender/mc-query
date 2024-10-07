docker build -t mc-query .
docker tag mc-query soulsender/mc-query:latest
docker push soulsender/mc-query:latest
