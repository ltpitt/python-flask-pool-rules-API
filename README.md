# README #

Pool rules API

### What is this repository for? ###

Http API written in Python and Flask to provide Pool Games rules stored in a SQLite db


### How do I get set up? ###

* Python (<3) is required. If you have Linux or Mac you should be good to go and you should skip to the next step, if you're on Windows get it from: http://ninite.com
* Clone the repository or simply download it as a zip file and unzip it on your pc
* Install all required components using pip (https://pip.pypa.io/en/latest/installing.html) with the following commands:
* pip install -r requirements.txt
* Launch the script with: python itemcatalog.py
* Open a web browser and visit: http://localhost:8000

### API Endpoints ###

It is possible to retrieve data in JSON format using the following urls:

##JSON##
* All catalog: http://localhost:8000/catalog/JSON
* Specific category: http://localhost:8000/catalog/INSERT_CATEGORY_ID/JSON
* Specific item: http://localhost:8000/catalog/INSERT_CATEGORY_ID/INSERT_ITEM_ID/JSON


### Contribution guidelines ###

* If you have any idea or suggestion contact directly the Repo Owner

### Who do I talk to? ###

* ltpitt: Repo Owner
