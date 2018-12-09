# pick-a-country

A simple web application based that fetches countries details like Capital, Population, Languages, Currency etc.

This is build on a python microframework Flask feeding off a Countries api. 


#Docker support
// to build image and create/recreate containers
docker-compose up -d --build --force-recreate -t 0

// added nginx conf to avoid port collision, a proxy server
nginx.conf

//to scale up as many containers
docker-compose up -d --scale <appname>=n (no. of containers)
