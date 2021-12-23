# nagp-unit-testing
## NAGP Unit Testing Assignment

### Setup
- Install python(pref. 3.8.x) and pip
- Install virtualenv using pip  -> pip install virtualenv(OPTIONAL)
- Create a virtual env -> python -m virtualenv my_venv(OPTIONAL)
- Activate the created my_venv using -> source my-venv/bin/activate(LINUX)(OPTIONAL)
- cd nagp-unit-testing
- pip install -r requirements.txt
- pip install -e .
> Virtualenv is not mandatory for code setup.

### Setting up Database
```sh
python database/database_setup.py
```
> Execute the above command before starting the application.

### Executing Test Cases
```sh
coverage run -m pytest -v test/ --cov=. --cov-report=html
```
> This generates a htmlcov holder inside the root folder i.e. nagp-unit-testing. Please use index.html inside that for checking the code coverage.

### Executing API
```sh
python app.py or python3 app.py
```
> This command starts the app on localhost:5000

### SwaggerUI
> For accessing the swagger ui, please visit localhost:5000 in web browser.

### Postman Collection
> Postman collection is stored as part of code in this repo. Please refer EBROKER COLLECTION.postman_collection.json

##### For screenshots and api routes please refer to the documentation in the Google Drive zip file.