# BSMCalculator
A Backend Calculator of Black-Scholes-Merton Model. Forked from previous project to be a standalone backend project.


# A small help to using Docker
Our API requires us to call the server and its port number. However Docker is often self enclosed.
What we need to do:

	````
	docker run -d -p HOST_PORT:CONTAINER_PORT <container-name>
	````

For example,
	
	docker run -d -p 0.0.0.0:8080 django-latest 
