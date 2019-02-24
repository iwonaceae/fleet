
# Overview
This is a REST API created in Python that returns 2 endpoints:


# Dependencies

Flask

To install use `pip`:


```bash

$ pip install Flask
```

# Version used

Python: 3.7.1

Flask: 1.0.2

# Run your app

1. Create a database and load some sample data:
In command prompt navigate to your project folder and run data_load.py:

```bash
$ python data_load.py
```

2. Start your app:

```bash
$ app.py flask run
```
Url:
http://localhost:8000/api/ships

#  Testing

In order to run the test you need to navigate to the file location and run it by calling unittest and passing the test file name as a parameter:

```bash

$ python -m unittest test.py
```