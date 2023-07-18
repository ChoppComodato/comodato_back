Steps for running the app:

1) download zip

2) extract zip

3) run command prompt (cmd) in extraction directory

4) create Python environment: `python -m venv venv`

5) activate environment: `.\venv\Scripts\activate`

6) install dependencies: `pip install -r requirements.txt`

7) set environment variable (if using PostgreSQL db): see env_example.txt

8) run application: `uvicorn app.src.main:app --reload`

9) in browser search for api documentation by URL: `localhost:8000/docs and localhost:8000/redoc`

10) run http package for loading data: app/database/seed_cliente.py 

11) load Postman collection for client-server manually interaction

12) run test in command prompt using: `pytest -vv`