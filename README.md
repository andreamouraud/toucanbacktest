# Toucan Toco backend test
## Introduction
This project is a [backend test](https://github.com/ToucanToco/backtechtest) for the Toucan Toco technical interview.

The goal is to create an API to obfuscate queries, save them to MongoDB then retrieve them from their ids only.

The API has been developed using Python3 and Flask and tests are run through pytest

The ids are generated using the Adler32 checksum algorithm, which creates an hashed integer that we convert to base 16, this approach has been chosen as it ensures the id will remain the same if we save two matching queries. Which avoids duplicates.

Documentation is only available with docstrings

I am not sure I understood the filters correctly, I can still change it if that is the case

## Installation and running
After cloning the repository, you can simply run the install script
```
./install.sh
python3 app.py
```
## Running the tests
Tests are done using pytest, make sure to be at the project root
```
py.test
```

## Usage
To start using the API, you'll first need to add your `config.cson` file containing all the queries in the root directory. The filename can be changed using the `cson` environment variable.

Once the API is started, you can retrieve all the generated query ids as follow:
```
curl -X GET -H "Content-Type: application/json" localhost:5000/queries
```
```
["3371131f","f9565cc7"]
```

You can then query the API to get the data:
```
curl -X POST -H "Content-Type: application/json" localhost:5000/query/3371131f
```
```
"{'domain': 'test_domain', 'my_key': '{{ my_filter }}'}"
```