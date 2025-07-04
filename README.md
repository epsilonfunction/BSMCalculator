# BSMCalculator
A Backend Calculator of Black-Scholes-Merton Model. Forked from previous project to be a standalone backend project.

# How It Works

Step 1: install requirements

    python3 -m venv .venv
    source .venv/bin/activate
    pip install uv
    uv install -r pyproject.toml

Step 2: Run Django Server in Developer mode

    cd bsm && python manage.py runserver

Step 3: Do an API call

Either, 
    
    curl -X POST {localserver}/api/calculate/ -H "Content-Type: application/json" -d '{"S": 100, "K": 100, "t": 1, "r": 0.05, "q": 0.02, "sigma": 0.2}'

Or, use the [[api_tester.ipynb]]

# A small help to using Docker
Our API requires us to call the server and its port number. However Docker is often self enclosed.
What we need to do:

	````
	docker run -d -p HOST_PORT:CONTAINER_PORT <container-name>
	````

For example,
	
	docker run -d -p 0.0.0.0:8080 django-latest 
